"""
AUMER Perplexity Client
Production-grade Perplexity SDK wrapper for all AUMER project use cases.

Requires: pip install perplexityai httpx
Env var: PERPLEXITY_API_KEY
"""

import os
import httpx
from perplexity import Perplexity, DefaultHttpxClient


# ---------------------------------------------------------------------------
# Client factory
# ---------------------------------------------------------------------------

def make_client() -> Perplexity:
    """Production client: retries, HTTP/2, connection pooling."""
    return Perplexity(
        max_retries=3,
        timeout=httpx.Timeout(connect=5.0, read=60.0, write=10.0, pool=10.0),
        http_client=DefaultHttpxClient(
            limits=httpx.Limits(
                max_keepalive_connections=20,
                max_connections=100,
                keepalive_expiry=30.0,
            ),
            http2=True,
        ),
    )


# ---------------------------------------------------------------------------
# 1. DAILY BRIEF  (n8n fires this at 7:30am Pacific)
# Uses: Agent API, pro-search preset
# Returns: plain text brief for Telegram/WhatsApp delivery
# ---------------------------------------------------------------------------

def daily_brief() -> dict:
    """
    Pull today\'s signals across VA policy, veteran deportations, DCAS,
    and active grant deadlines. Called by n8n Workflow 1.
    """
    client = make_client()

    response = client.responses.create(
        preset="pro-search",
        input=(
            "Search today for developments in ALL of the following areas and "
            "return one paragraph per topic (skip topics with no new results):\n"
            "1. VA policy changes affecting non-citizen veteran benefits\n"
            "2. DHS/ICE deportation of U.S. military veterans\n"
            "3. DCAS or Pentagon Vietnam casualty record updates\n"
            "4. NEH, Ford Foundation, MacArthur Foundation grant deadlines or announcements\n"
            "5. Congressional action on veteran citizenship or benefits legislation\n"
            "Return only factual findings with source URLs. "
            "If no new information found for a topic, omit it entirely."
        ),
    )
    return {
        "content": response.output_text,
        "model": response.model,
    }


# ---------------------------------------------------------------------------
# 2. FOIA WATCHDOG  (weekly, monitors .gov sites for policy changes)
# Uses: Sonar API with domain + recency filters
# ---------------------------------------------------------------------------

def foia_watchdog() -> dict:
    """
    Monitor VA, DHS, ICE, USCIS for policy changes affecting FOIA case.
    search_domain_filter restricts results to government sources only.
    """
    client = make_client()

    queries = [
        (
            "What new guidance or policy changes has the VA issued about "
            "non-citizen veteran benefits, XC-files, or alien claims in the past 7 days?",
            ["va.gov", "benefits.va.gov"],
        ),
        (
            "What new ICE or DHS enforcement policies affect U.S. military veterans "
            "in removal proceedings in the past 7 days?",
            ["dhs.gov", "ice.gov", "uscis.gov"],
        ),
    ]

    results = []
    for query_text, domains in queries:
        completion = client.chat.completions.create(
            model="sonar-pro",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Only answer using the search results provided. "
                        "If the results do not contain new policy changes, "
                        "say so explicitly rather than guessing. "
                        "State the source URL for each finding."
                    ),
                },
                {"role": "user", "content": query_text},
            ],
            search_domain_filter=domains,
            search_recency_filter="week",
        )
        results.append({
            "query": query_text,
            "answer": completion.choices[0].message.content,
            "citations": getattr(completion, "citations", []),
        })

    return {"watchdog_results": results}


# ---------------------------------------------------------------------------
# 3. SUBMISSION CONCIERGE  (before each institution letter is drafted)
# Uses: Agent API with web_search tool + Claude as the model
# Looks up current submission guidelines BEFORE drafting the letter
# ---------------------------------------------------------------------------

def research_institution(institution_name: str, institution_url: str = "") -> dict:
    """
    Before drafting a submission letter, look up the institution\'s
    current submission guidelines, contact info, and relevant collections.
    """
    client = make_client()

    query = (
        f"Look up current submission guidelines and contact information for "
        f"{institution_name}\'s special collections, archives, or veterans history program. "
        f"Return: (1) current submission contact name and email, "
        f"(2) any submission format requirements, "
        f"(3) whether they have a veterans, Chicano, or ethnic studies collection, "
        f"(4) any current deadlines or call for submissions."
    )
    if institution_url:
        query += f" Check their website at {institution_url} first."

    response = client.responses.create(
        model="anthropic/claude-sonnet-4-6",
        input=query,
        tools=[{"type": "web_search"}],
        instructions=(
            "Search the institution\'s website and any recent announcements. "
            "Return only verified, current information. "
            "If contact info is not found, say so explicitly."
        ),
    )
    return {
        "institution": institution_name,
        "research": response.output_text,
    }


# ---------------------------------------------------------------------------
# 4. GRANT RESEARCH  (before each grant application is drafted)
# Uses: Agent API, pro-search preset
# ---------------------------------------------------------------------------

def research_grant_funder(funder_name: str, program_name: str, year: int = 2026) -> dict:
    """
    Research a grant funder\'s current priorities before writing the application.
    """
    client = make_client()

    response = client.responses.create(
        preset="pro-search",
        input=(
            f"Research {funder_name}\'s {program_name} grant program for {year}. "
            f"Return: (1) current funding priorities and focus areas, "
            f"(2) recent grants awarded in the past 2 years and their amounts, "
            f"(3) submission deadline and any changes from prior years, "
            f"(4) program officer name and contact if available, "
            f"(5) any stated interest in veteran, immigration, or Latino/Chicano research."
        ),
    )
    return {
        "funder": funder_name,
        "program": program_name,
        "research": response.output_text,
    }


# ---------------------------------------------------------------------------
# 5. ACADEMIC CITATION LOOKUP  (for manuscript footnotes and grant narratives)
# Uses: Sonar with academic domain filters
# ---------------------------------------------------------------------------

def find_academic_citations(claim: str, max_results: int = 5) -> dict:
    """
    Find peer-reviewed citations supporting a specific claim.
    Used to strengthen grant narratives and manuscript footnotes.
    """
    client = make_client()

    completion = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {
                "role": "system",
                "content": (
                    "Only return peer-reviewed academic sources. "
                    "Format each citation as: Author(s), Title, Journal, Year, DOI if available. "
                    f"Return no more than {max_results} citations. "
                    "If fewer than 3 high-quality sources exist, say so explicitly."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Find peer-reviewed academic sources supporting this claim: {claim}. "
                    f"Focus on sources from sociology, history, public policy, "
                    f"or legal scholarship. Prioritize sources from 2000-present."
                ),
            },
        ],
        search_domain_filter=[
            "scholar.google.com", "jstor.org", "pubmed.ncbi.nlm.nih.gov",
            "ssrn.com", "semanticscholar.org", "arxiv.org",
        ],
        search_recency_filter="year",
    )
    return {
        "claim": claim,
        "citations": completion.choices[0].message.content,
        "sources": getattr(completion, "citations", []),
    }


# ---------------------------------------------------------------------------
# 6. CONCISE STREAM HANDLER  (for Base44 interactive agents)
# Uses: Sonar Pro with concise streaming
# Shows reasoning steps in real time - good for Base44 agent UX
# ---------------------------------------------------------------------------

class AUMERStreamHandler:
    """Concise streaming handler for Base44 Superagent interfaces."""

    def __init__(self):
        self.content = ""
        self.reasoning_steps = []
        self.search_results = []
        self.usage = None
        self.total_cost = 0.0

    def query(self, user_message: str, system_prompt: str = "") -> dict:
        client = make_client()
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})

        stream = client.chat.completions.create(
            model="sonar-pro",
            messages=messages,
            stream=True,
            stream_mode="concise",
        )

        chunk_handlers = {
            "chat.reasoning": self._handle_reasoning,
            "chat.reasoning.done": self._handle_reasoning_done,
            "chat.completion.chunk": self._handle_content,
            "chat.completion.done": self._handle_done,
        }

        for chunk in stream:
            handler = chunk_handlers.get(chunk.object)
            if handler:
                handler(chunk)

        return {
            "content": self.content,
            "reasoning_steps": self.reasoning_steps,
            "search_results": self.search_results,
            "total_cost": self.total_cost,
        }

    def _handle_reasoning(self, chunk):
        delta = chunk.choices[0].delta
        if hasattr(delta, "reasoning_steps"):
            for step in delta.reasoning_steps:
                self.reasoning_steps.append(step)

    def _handle_reasoning_done(self, chunk):
        if hasattr(chunk, "search_results"):
            self.search_results = chunk.search_results

    def _handle_content(self, chunk):
        delta = chunk.choices[0].delta
        if hasattr(delta, "content") and delta.content:
            self.content += delta.content

    def _handle_done(self, chunk):
        if hasattr(chunk, "usage"):
            self.usage = chunk.usage
            if hasattr(chunk.usage, "cost"):
                self.total_cost = chunk.usage.cost.total_cost


# ---------------------------------------------------------------------------
# CLI test  (run directly to verify your API key works)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Testing AUMER Perplexity client...")
    print(f"API key set: {'yes' if os.getenv('PERPLEXITY_API_KEY') else 'NO - set PERPLEXITY_API_KEY first'}")

    if os.getenv("PERPLEXITY_API_KEY"):
        result = research_grant_funder("NEH", "Scholarly Editions and Translations")
        print("\n--- NEH Research ---")
        print(result["research"][:500])
