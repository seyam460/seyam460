from playwright.sync_api import sync_playwright
import pandas as pd
import time

def scrape_google_maps(query):
    leads = []

    with sync_playwright() as p:
        # Browser খুলবে — তুমি দেখতে পাবে
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print(f"🔍 Searching: {query}")

        # Google Maps এ যাও
        search_url = f"https://www.google.com/maps/search/{query.replace(' ', '+')}"
        page.goto(search_url)
        time.sleep(4)

        # Left side এ results আছে — সেটা scroll করো
        for _ in range(8):
            page.locator('div[role="feed"]').press("PageDown") 
            time.sleep(1.5)

        # সব business link নাও
        listings = page.locator('a[href*="/maps/place/"]').all()
        print(f"📍 Found {len(listings)} listings")

        for listing in listings:
            try:
                name = listing.get_attribute("aria-label")
                href = listing.get_attribute("href")

                if name and href:
                    # প্রতিটা business এ click করো details আনতে
                    listing.click()
                    time.sleep(2.5)

                    # Website আছে কিনা চেক করো
                    website_btn = page.locator('a[data-item-id="authority"]')
                    
                    has_website = website_btn.count() > 0

                    if not has_website:
                        # Phone number নাও
                        phone = "N/A"
                        phone_btn = page.locator('button[data-item-id*="phone"]')
                        if phone_btn.count() > 0:
                            phone = phone_btn.first.get_attribute("aria-label")
                            phone = phone.replace("Phone:", "").strip() if phone else "N/A"

                        leads.append({
                            "Business": name,
                            "Phone": phone,
                            "Website": "নেই ❌"
                        })
                        print(f"  ✅ {name} | {phone}")
                    else:
                        print(f"  ⏭️ Skipped (has website): {name}")

            except Exception as e:
                print(f"  ⚠️ Error: {e}")
                continue

        browser.close()

    return leads


# ─── Main ───
all_leads = []

# যেসব category খুঁজবে
searches = [
    "restaurant Dhaka Bangladesh",
    "pharmacy Mirpur Dhaka",
    "clinic Uttara Dhaka",
    "coaching center Dhanmondi Dhaka"
]

for query in searches:
    results = scrape_google_maps(query)
    all_leads.extend(results)
    print(f"\n⏳ Waiting before next search...\n")
    time.sleep(5)

# ─── Save ───
if all_leads:
    df = pd.DataFrame(all_leads)
    df.to_csv("leads.csv", index=False, encoding="utf-8-sig")
    print(f"\n🎯 Total Leads: {len(all_leads)}")
    print("📁 Saved → leads.csv ✅")
else:
    print("\n⚠️ কোনো lead পাওয়া যায়নি")