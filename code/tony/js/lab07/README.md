# Overview

## User Stories

### User One
As a user, I want to search emoji by keyword, because I don't like my OS' emoji finder.

### User Two
As a user, I want to see more detailed information about emojis, such as version number, because I am interested in the technical history.

# R&D Notes

Because Unicode.org does not include the Access-Control-Allow-Origin header, I needed to mirror the Emoji data on GitHub, which includes Access-Control-Allow-Origin: *, enabling the browser to handle CORS under its own security restrictions.

## Links

### Emoji Data from Unicode Consortium
https://unicode.org/Public/emoji/15.0/emoji-test.txt

### My mirror of the Unicode data (above)
https://raw.githubusercontent.com/webavant/data/main/emoji-test.txt
