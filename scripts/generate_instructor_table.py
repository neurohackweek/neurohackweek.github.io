instructors = [
    ('Ariel Rokem', 'http://arokem.org/', 'University of Washington', 'Director'),
    ('Tal Yarkoni', 'http://talyarkoni.org', 'University of Texas at Austin', 'Co-Director'),
    ('Deanna Barch', 'https://psychweb.wustl.edu/people/deanna-barch', 'Washington University in St. Louis'),
    ('Bing Brunton', 'https://bingbrunton.com', 'University of Washington'),
    ('Cameron Craddock', 'https://dellmed.utexas.edu/team-profile/cameron-craddock', 'University of Texas at Austin'),
    ('Eva Dyer', 'https://bme.gatech.edu/bme/faculty/Eva-Dyer', 'Georgia Tech'),
    ('Satra Ghosh', 'http://satra.cogitatum.org/', 'MIT'),
    ('Chris Gorgolewski', 'http://reproducibility.stanford.edu/team/chris-gorgolewski/', 'Stanford University'),
    ('Anisha Keshavan', 'http://ilabs.washington.edu/postdoctoral-fellows/bio/i-labs-anisha-keshavan', 'University of Washington'),
    ('Eran Klein', 'https://phil.washington.edu/people/eran-klein', 'University of Washington'),
    ('Fernando Perez', 'https://bids.berkeley.edu/people/fernando-perez', 'University of California Berkeley'),
    ('Russell Poldrack', 'https://poldracklab.stanford.edu/', 'Stanford University'),
    ('JB Poline', 'https://www.mcgill.ca/qls/researchers/jb-poline', 'McGill University'),
    ('Jake Vanderplas', 'http://escience.washington.edu/people/jake-vanderplas/', 'University of Washington'),
    ('Gael Varoquaux', 'http://gael-varoquaux.info/', 'INRIA'),
    ('Tor Wager', 'https://wagerlab.colorado.edu', 'University of Colorado Boulder'),
    ('Kirstie Whitaker', 'https://whitakerlab.github.io/', 'Turing Institute'),
]

tr_template = "<tr>%s\n</tr>\n"

td_template = """
<td class="thumb"><img src="img/instructors/{image}.jpg"></td>
<td><a href="{url}">{name}</a>{title}<br />{affil}</td>"""

html = ''
tr = ''

for i, person in enumerate(instructors):
    name = person[0]
    url = person[1]
    affil = person[2]
    title = ' (%s)' % person[3] if len(person) > 3 else ''
    image = name.split(' ')[-1].lower()
    tr += td_template.format(name=name, affil=affil, title=title, url=url,
                            image=image)
    if (i and i % 2) or (i + 1) == len(instructors):
        html += tr_template % tr
        tr = ''

print(html)
