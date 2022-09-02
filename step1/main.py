# Question 1 Solution
import os;
import re;

fakedoc = """
                XXXXXX, XXXXXXX
                ##########
                Ronald Reagan UCLA Medical Center
                XXXXX 
                XXXXX, CA 90095 4444
                Date 06/05/2020

NEUROLOGY AND PAIN MEDICINE
INITIAL OUTPATIENT NOTE

XXXXXX, XXXXXX
PATIENT HISTORY
Ms. XXXXXX is a 40y women seen in consultation at the request of Dr. XXXXXXXXXX. The patient is alert 
and orinted to self, place and cirumstance. She self-reports stress due her two pregancies that has 
only be reduced somewhat by stepping back from her royal duties in Jan. 

Consitution: Well developed, well nourished WF in no apparent distress.

Assessment: Neuropathic pain, stress

TREATMENT/PLAN:
Rx for compounded gel containing ketamine, baclofen, imipramine, gabapentin and tetracaine.
Suggested finding more time for exercise and sleep for stress

REFERRING PHYSICIAN
XXXXXX, XXXXXX, MD

Electronially signed by XXXXXX, XXXXXX DO, PhD on 06/06/2020
"""

# Write regular expression/s here, be as general as possible with your regular expression

date_p = r"\d{1,2}\/\d{1,2}\/\d{4}"
pattern_date = re.compile(date_p)
fakedoc = pattern_date.sub(r'XX/XX/XXXX', fakedoc)

state = ['CA', 'MD']
location_p = r"(CA"
for s in state:
    location_p = location_p + '|' + s
location_p += ")(\s)?(\d{5})?"
# location_p = "(MD|CA)(\s)?(\d{5})?"
pattern_location = re.compile(location_p)
fakedoc = pattern_location.findall(fakedoc)

# Output the fake document
print(fakedoc)
