[link.bm_factory(nm="special_sections" t="Cover, Revision &amp; Contract Sections")]
[link.special_sections]
##Cover, Revision & Contact Sections

There are three (3) specialized sections that can be defined within your document to add commonly used information in script files. They are:

{:.indent}###var.cover - To add a cover section
{:.indent}###@var.revision - To add a revision section
{:.indent}###@var.contact - To add a contact section

The details for each type of section are as follows:

### Cover Title

{:.syntax}@@@ divTitle Cover Title Syntax
    &nbsp;
    {:.indent}var.cover title="title of script" author="written by" logline="logline or short description"

Each element is optional, and they can appear in any order. Also note that the value of any parameter can be whatever you want. Just because it says "author", doesn't mean you have to put the author name there. You could instead write "Roses are Red", and that would be just fine...

###var.revision v="revision"
Specify the revision number of your document within quotes. The default rendering of the var.revision variable is to include a timestamp at the end of the string. You can request a plain revision string using the vp attribute e.g. [var.revision.vp]

###var.contact cn="name" ph="phone" em="email" c1="copyright line 1" c2="copyright line 2" c3="copyright line 3"

Each element is optional, and the elements can appear in any order. By default, the system looks in the var.defaults variable for the definitions of cn, ph, em, c1, c2 & c3. As such, you can conveniently set them using a single call:

.**@set _id="defaults"\
     cn="Ken Lowrie"\
     ph="*512-710-7257*"\
     em="[ken@cloudylogic.com]"\
     c1="Copyright © 2018 Cloudy Logic Studios, LLC."\
     c2="All Rights Reserved."\
     c3="[www.cloudylogic.com]"**

@set _id="defaults"\
     cn="Ken Lowrie"\
     ph="*512-710-7257*"\
     em="[ken@cloudylogic.com]"\
     c1="Copyright © 2018 Cloudy Logic Studios, LLC."\
     c2="All Rights Reserved."\
     c3="[www.cloudylogic.com]"

To see these tags in action, take a look at the userguideheading.md document in the import folder of this user guide.

[link.special_sections.link]
// And now let's try various versions

[var.cover._inline_(title="Title of Script" author="Script Author")]
[var.cover._inline_(title="Title of Script" author="Script Author" logline="Logline")]
[var.cover._inline_(author="Script Author")]
[var.cover._inline_(logline="Logline")]
[var.cover._inline_(author="Script Author" logline="Logline")]
[var.cover._inline_(title="Title of Script" logline="Logline")]
[var.cover._inline_(title="Title of Script")]
[var.cover._inline_(title="" author="Script Author" logline="")]
[var.cover(title =     "Title of Script" author   =   "Script Author")]
[var.cover(title="Title of Script" author  ="Script Author" logline=  "Logline")]
[var.cover(     author    =    "Script Author"    )]
[var.cover]
[var.cover( author="author")]
[var.cover(author="author" title="title" logline="logline")]

Note that we'll always use timestamp off in the unittest scripts, because otherwise the comparison will fail... The code is unit tested separately...

[var.revision._inline_plain_(v="1.0")]
[var.revision._inline_plain_(v="1.1")]
[var.revision.plain]
 
[var.contact]  
[var.contact(cn="")]
[var.contact(ph="")]
[var.contact(em="")]
[var.contact(c1="")]
[var.contact(c2="")]
[var.contact(c3="" )]
[var.contact(cn="cn"  c2="c2")]
[var.contact(c2=""  cn="")]

[var.contact._inline_(cn ="Contact Name"   )]   
[var.contact._inline_(ph="210-555-1212"   )]  
[var.contact._inline_(cn="Contact Name2" ph="210-555-1212"   )]  
[var.contact._inline_(em="email@mydomain.com"    )]
[var.contact._inline_(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1" )]
[var.contact._inline_(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2")]
[var.contact._inline_(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3")]

[var.contact( ph="210-555-5309" em="" c1="" c2="" c3=""    )]
[var.contact( ph="210-555-1212" em="email@mydomain.com"    )]
[var.contact( ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1" )]
[var.contact( ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2"   )]
[var.contact( ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]

[var.contact._inline_(  em="EMAIL@mydomain.com"    )]
[var.contact._inline_(  em="email@mydomain.com" c1="Copyright  Line 1a"     )]
[var.contact._inline_(  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2b"   )]
[var.contact._inline_(  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3c" )]

[var.contact(   c1="Copyright  Line 1a"  )]
[var.contact(   c1="Copyright  Line 1"  c2="Copyright Line 2b" )]
[var.contact(   c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3c" )]

[var.contact(    c2="Copyright Line 2")]
[var.contact(    c2="Copyright Line 2" c3="Copyright Line 3" )]

[var.contact(     c3="Copyright Line 3" )]

[var.contact._inline_( ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact._inline_(cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact._inline_(cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact._inline_(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact._inline_(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c3="Copyright Line 3" )]
[var.contact._inline_(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2")]

[var.contact(  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact( ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact( ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact( ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c3="Copyright Line 3" )]
[var.contact( ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2")]


[var.contact._inline_(cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" )]c3="Copyright Line 3" 
[var.contact._inline_(cn="Contact Name"   c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact._inline_(cn="Contact Name"  em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact._inline_(cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c3="Copyright Line 3" )]
[var.contact._inline_(cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2")]

[var.contact(cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact(cn="Contact Name" ph="210-555-1212"   c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact(cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c3="Copyright Line 3" )]
[var.contact(cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2")]

[var.contact._inline_(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact._inline_(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com"   c3="Copyright Line 3" )]
[var.contact._inline_(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2")]

[var.contact._inline_(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c3="Copyright Line 3" )]
[var.contact._inline_(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1" )]

[var.contact(cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact(cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c3="Copyright Line 3" )]
[var.contact(cn="Contact Name"   c1="Copyright  Line 1"  c3="Copyright Line 3" )]
[var.contact(cn="Contact Name"   c1="Copyright  Line 1"  )]

[var.contact._inline_(cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact._inline_(cn="Contact Name" ph="210-555-1212"   c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact._inline_(cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c3="Copyright Line 3" )]
[var.contact._inline_(cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2")]


[var.contact( ph="210-444-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact( ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact( ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact( ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1b"  c3="Copyright Line 3" )]
[var.contact._inline_( ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2")]
[var.contact._inline_(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact._inline_(cn="Contact Name" ph="210-555-1212"   c2="Copyright Line 2c" c3="Copyright Line 3" )]
[var.contact._inline_(cn="Contact Name"  em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" )]

@dump var=".*" link="b"