import json
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) > 1: # we check if we received any argument
        if sys.argv[1] == "supports": 
            # then we are good to return an exit status code of 0, since the other argument will just be the renderer's name
            sys.exit(0)

    # load both the context and the book representations from stdin
    context, book = json.load(sys.stdin)
    # and now, we can just modify the content of the first chapter
    # book['sections'][0]['Chapter']['Content'] = '# Hello'
    for (i, section) in enumerate(book['sections']):
        if 'Chapter' in section: 
            content: str = section['Chapter']['content']

            # Find download macro
            idx = content.find("[download=")
            # Make sure it is not escaped
            if idx != -1 and content[idx - 2:idx] != '\\\\':
                # Grab first part of content excluding the macro
                before = content[:idx]
                after = content[idx:]
                # Find where macro ends
                end_idx = after.find("]")
                # Ensure macro does end, i.e. it is properly formatted
                if end_idx != -1:
                    # Get whole macro
                    whole = after[:end_idx]
                    # Get second part of content excluding macro and skipping trailing ]
                    after = after[end_idx+1:]
                    # Extract link from macro
                    [_, link] = whole.split("=")

                    with requests.get(link) as data:
                        link = data.content.decode()

                    # Update content
                    book['sections'][i]['Chapter']['content'] = before + link + after


    # we are done with the book's modification, we can just print it to stdout, 
    print(json.dumps(book))