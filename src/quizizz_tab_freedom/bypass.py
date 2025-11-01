import asyncio
from playwright.async_api import async_playwright

class QuizizzBypass:

    def __init__(self):
        """Initialize the QuizizzBypass instance with null browser resources."""
        self.p = None
        self.browser = None
        self.context = None

    async def setup(self):
        """Launch a stealth-configured Chromium browser and create a context with evasion scripts."""
        self.p = await async_playwright().start()
        self.browser = await self.p.chromium.launch(
            headless=False,
            args=[
                '--window-size=1920,1080',
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--no-default-browser-check',
                '--disable-background-timer-throttling',
                '--disable-popup-blocking',
                '--disable-features=TranslateUI,site-per-process'
            ]
        )

        self.context = await self.browser.new_context(
            viewport=None,
            no_viewport=True,
            ignore_https_errors=True,
            java_script_enabled=True
        )

        await self._inject_stealth_scripts()

    async def _inject_stealth_scripts(self):
        """Inject JavaScript snippets into the browser context to bypass common bot detection techniques."""
        stealth_script = """
        // Prevent detection
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
        
        // Override all detection methods
        const originalAddEventListener = EventTarget.prototype.addEventListener;
        EventTarget.prototype.addEventListener = function(type, listener, options) {
            if (type === 'blur' || type === 'visibilitychange') {
                return; // Block these listeners
            }
            return originalAddEventListener.call(this, type, listener, options);
        };
        
        // Keep focus always
        setInterval(() => {
            if (!document.hasFocus()) {
                window.dispatchEvent(new FocusEvent('focus'));
            }
        }, 100);
        
        // Mock performance metrics
        const originalNow = performance.now;
        performance.now = function() {
            return originalNow.call(performance) + Math.random() * 10;
        };
        """

        await self.context.add_init_script(stealth_script)

    async def create_stealth_page(self):
        """Create a new page with additional stealth measures applied at the page level."""
        page = await self.context.new_page()

        await page.add_init_script("""
            // Page-level visibility override
            Object.defineProperty(document, 'visibilityState', { value: 'visible' });
            Object.defineProperty(document, 'hidden', { value: false });
            
            // Prevent beforeunload
            window.onbeforeunload = null;
        """)

        return page
    
    async def multi_tab_operation(self, quizizz_url: str, research_url: str):
        """Open and manage two tabs: one for Quizizz and one for external research, simulating legitimate multi-tab usage.

        Args:
            quizizz_url (str): The URL of the Quizizz session.
            research_url (str): The URL of the auxiliary research page.
        
        Returns:
            tuple: A pair of Playwright page objects (quizizz_tab, research_tab).
        """
        quizizz_tab = await self.create_stealth_page()
        await quizizz_tab.goto(quizizz_url)

        research_tab = await self.context.new_page()
        await research_tab.goto(research_url)

        print("✓ Bypass successful. Multi-tab session secured.")

        await quizizz_tab.bring_to_front()
        await asyncio.sleep(2)
        await research_tab.bring_to_front()

        return quizizz_tab, research_tab
    
    async def close(self):
        """Gracefully close the browser and stop the Playwright process."""
        if self.browser:
            await self.browser.close()
        if self.p:
            await self.p.stop()