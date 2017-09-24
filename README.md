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
- [ ] store requirements page for each donation center and regularly ping to compare to cached copy to detect changes
- [ ] autocomplete suggestions (as user types in text box) drawn from eligible items
- [ ] NLP to identify similar items and synonyms in order to operationalize a search bar, item-level approach
