instructors = [
    ('Ariel Rokem', 'http://arokem.org/', 'eScience Institute', 'University of Washington', 'Director'),
    ('Tal Yarkoni', 'http://talyarkoni.org', 'Department of Psychology', 'University of Texas at Austin', 'Co-Director'),
    ('Deanna Barch', 'https://psychweb.wustl.edu/people/deanna-barch', 'Department of Psychological and Brain Sciences', 'Washington University in St. Louis'),
    ('Bing Brunton', 'https://bingbrunton.com', 'Department of Biology', 'University of Washington'),
    ('Cameron Craddock', 'https://dellmed.utexas.edu/team-profile/cameron-craddock', 'Diagnostic Medicine', 'University of Texas at Austin'),
    ('Eva Dyer', 'https://bme.gatech.edu/bme/faculty/Eva-Dyer', 'Department of Biomechanical Engineering', 'Georgia Tech'),
    ('Satra Ghosh', 'http://satra.cogitatum.org/', 'McGovern Institute for Brain Research', 'MIT'),
    ('Chris Gorgolewski', 'http://reproducibility.stanford.edu/team/chris-gorgolewski/', 'Department of Psychology', 'Stanford University'),
    ('Anisha Keshavan', 'http://ilabs.washington.edu/postdoctoral-fellows/bio/i-labs-anisha-keshavan', 'eScience Institute', 'University of Washington'),
    ('Sanmi Koyejo', 'http://sanmi.cs.illinois.edu/', 'Department of Computer Science', 'University of Illinois at Urbana-Champaign'),
    ('Eran Klein', 'https://phil.washington.edu/people/eran-klein', 'Department of Philosophy', 'University of Washington'),
    ('Fernando Perez', 'https://bids.berkeley.edu/people/fernando-perez', 'Department of Statistics', 'University of California Berkeley'),
    ('Russell Poldrack', 'https://poldracklab.stanford.edu/', 'Department of Psychology', 'Stanford University'),
    ('JB Poline', 'https://www.mcgill.ca/qls/researchers/jb-poline', 'Neurology and Neurosurgery', 'McGill University'),
    ('Jake Vanderplas', 'http://escience.washington.edu/people/jake-vanderplas/', 'eScience Institute', 'University of Washington'),
    ('Gael Varoquaux', 'http://gael-varoquaux.info/', 'Neurospin', 'INRIA'),
    ('Tor Wager', 'https://wagerlab.colorado.edu', 'Department of Psychology & Neuroscience', 'University of Colorado Boulder'),
    ('Kirstie Whitaker', 'https://whitakerlab.github.io/', 'Turing Institute', ''),
]

tr_template = "<tr>%s\n</tr>\n"

td_template = """
<td class="thumb"><img src="img/instructors/{image}.jpg"></td>
<td><a href="{url}">{name}</a>{title}<br />{dept}<br />{inst}</td>"""

html = ''
tr = ''

for i, person in enumerate(instructors):
    name, url, dept, inst = person[:4]
    title = ' (%s)' % person[4] if len(person) > 4 else ''
    image = name.split(' ')[-1].lower()
    tr += td_template.format(name=name, inst=inst, title=title, url=url,
                            image=image, dept=dept)
    if (i and i % 2) or (i + 1) == len(instructors):
        html += tr_template % tr
        tr = ''

print(html)
