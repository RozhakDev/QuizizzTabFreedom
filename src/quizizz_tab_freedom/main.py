import argparse
import asyncio
from .bypass import QuizizzBypass

async def main():
    """Parse command-line arguments and orchestrate a multi-tab Quizizz session with a research tab using stealth automation.

    The function initializes the QuizizzBypass class, sets up a stealth browser context,
    opens two tabs—one for Quizizz and one for research—and keeps the session active
    until user input terminates the program.

    Command-line arguments:
        --quizizz-url (str): URL of the Quizizz session. Defaults to 'https://quizizz.com'.
        --research-url (str): URL for auxiliary research. Defaults to 'https://google.com'.

    Note:
        Intended for educational and ethical use only. Requires manual termination via Enter key.
    """
    parser = argparse.ArgumentParser(
        description="QuizizzTabFreedom: Ethical automation tool for tab freedom in Quizizz sessions. "
                    "Designed for PC-based research and productivity enhancement. "
                    "Use responsibly for educational purposes only."
    )

    parser.add_argument(
        '--quizizz-url',
        type=str,
        default='https://quizizz.com',
        help='URL for the Quizizz session (optional, e.g., https://quizizz.com/join?gc=070467 or https://wayground.com/join?gc=070467)'
    )
    parser.add_argument(
        '--research-url',
        type=str,
        default='https://google.com',
        help='URL for the research tab (optional, e.g., https://grok.com or https://chatgpt.com for productivity)'
    )

    args = parser.parse_args()

    bypass = QuizizzBypass()
    await bypass.setup()
    quiz_tab, research_tab = await bypass.multi_tab_operation(
        quizizz_url=args.quizizz_url,
        research_url=args.research_url
    )

    input("Testing in progress... Press Enter to exit")
    await bypass.close()

if __name__ == "__main__":
    asyncio.run(main())