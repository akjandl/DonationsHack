# DonationsHack

## Idea
website that allows you to input an item you want to donate, and it provides the names, locations, and hours of donation centers that accept this item.
Behavior:
- enter item into text box
- if accepted item, list location details where to donate
- if not donatable, show links for:
    -freecycle
    - craigslist
    - city/town webpages with list of things that can be disposed of
    - waste management/large item pick-up

## MVP To Do
- [x] retrieve data around items accepted by location and location metadata (e.g., hours)
- [x] create sqlite database
- [x] create first-pass webpage
- [x] create first-pass flask app controller logic

## Extensions
- [ ] navbar with category dropdown, locations dropdown, and info/about
- [ ] store requirements page for each donation center and regularly ping to compare to cached copy to detect changes
- [ ] autocomplete suggestions (as user types in text box) drawn from eligible items
- [ ] implement item/category seacrh box
    - [ ] NLP to identify similar items and synonyms in order to operationalize a search bar, item-level approach
        - [ ] incorporate user feedback into NLP item-category mapping model
    - [ ] use search data to identify highly avialable goods and common pain points
- [ ] allow donation locations to submit corrections
- [ ] allow donation locations to submit highly needed items
- [ ] add content around where to dispose of things (e.g., paint)
- [ ] add alternative ways of getting rid of stuff (e.g., CL, ebay, freecycle, etc.)
- [ ] geo-filtered results
