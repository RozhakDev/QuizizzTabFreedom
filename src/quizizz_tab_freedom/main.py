import argparse
import asyncio
from .bypass import QuizizzBypass

async def main():
    
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