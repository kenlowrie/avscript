@+[special+sections]
##Cover, Revision & Contact Sections

There are three (3) specialized sections that can be defined within your document to add commonly used information in script files. They are:

{:.indent}###@cover - To add a cover section
{:.indent}###@revision - To add a revision section
{:.indent}###@contact - To add a contact section

The details for each type of section are as follows:

### Cover Title

{:.syntax}@@@ divTitle Cover Title Syntax
    &nbsp;
    {:.indent}@cover title="title of script" author="written by" logline="logline or short description"

Each element is optional, and they can appear in any order. Also note that the value of any parameter can be whatever you want. Just because it says "author", doesn't mean you have to put the author name there. You could instead write "Roses are Red", and that would be just fine...

###@revision v="revision" timestamp="yes"
Specify the revision number of your document within the angle brackets. If timestamp is either not specified or has any value other than "No", "Off", "False" or "0", the current date and time of the document at the time of processing will also be inserted immediately following the revision number. This provides additional clarification of the version, in case you forget to bump the version number.

If you specify timestamp="No" | "Off" | "False" | "0", then the timestamp will not be added to the revision string.

###@contact cn="name" ph="phone" em="email" c1="copyright line 1" c2="copyright line 2" c3="copyright line 3"

Each element is optional, and the elements can appear in any order.

To see these tags in action, take a look at the userguideheading.md document in the import folder of this user guide.

// And now let's try various versions

@cover title="Title of Script" author="Script Author"
@cover title="Title of Script" author="Script Author" logline="Logline"
@cover author="Script Author"
@cover logline="Logline"
@cover author="Script Author" logline="Logline"
@cover title="Title of Script" logline="Logline"
@cover title="Title of Script"
@cover title="" author="Script Author" logline=""

@cover title =     "Title of Script" author   =   "Script Author"
@cover   title="Title of Script" author  ="Script Author" logline=  "Logline"
@cover      author    =    "Script Author"    
@cover
@cover author="author"
@cover author="author" title="title" logline="logline"

Note that we'll always use timestamp off in the unittest scripts, because otherwise the comparison will fail... Need to handle that a different way for testing...

@revision timestamp="no"
@revision v="1.0" timestamp="False"
@revision v="1.1" timestamp="0"
 @revision
 @ revision
@revision v="" timestamp="OFF"


@contact  
@contact cn=""
@contact ph=""
@contact em=""
@contact c1=""
@contact c2=""
@contact c3="" 
@contact cn=""  c2=""
@contact c2=""  cn=""

@contact cn ="Contact Name"      
@contact cn="Contact Name" ph="210-555-1212"     
@contact cn="Contact Name" ph="210-555-1212" em="email@mydomain.com"    
@contact cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1" 
@contact cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2"
@contact cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3"

@contact  ph="210-555-1212"     
@contact  ph="210-555-1212" em="email@mydomain.com"    
@contact  ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1" 
@contact  ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2"   
@contact  ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" 

@contact   em="email@mydomain.com"    
@contact   em="email@mydomain.com" c1="Copyright  Line 1"     
@contact   em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2"   
@contact   em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" 

@contact    c1="Copyright  Line 1"  
@contact    c1="Copyright  Line 1"  c2="Copyright Line 2" 
@contact    c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" 

@contact     c2="Copyright Line 2"
@contact     c2="Copyright Line 2" c3="Copyright Line 3" 

@contact      c3="Copyright Line 3" 

@contact  ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact cn="Contact Name" ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c3="Copyright Line 3" 
@contact cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2"

@contact   em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact  ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact  ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact  ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c3="Copyright Line 3" 
@contact  ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2"


@contact cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact cn="Contact Name"   c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact cn="Contact Name"  em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c3="Copyright Line 3" 
@contact cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2"

@contact cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact cn="Contact Name" ph="210-555-1212"   c2="Copyright Line 2" c3="Copyright Line 3" 
@contact cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c3="Copyright Line 3" 
@contact cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2"

@contact cn="Contact Name" ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact cn="Contact Name" ph="210-555-1212" em="email@mydomain.com"   c3="Copyright Line 3" 
@contact cn="Contact Name" ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2"

@contact cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c3="Copyright Line 3" 
@contact cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1" 

@contact cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c3="Copyright Line 3" 
@contact cn="Contact Name"   c1="Copyright  Line 1"  c3="Copyright Line 3" 
@contact cn="Contact Name"   c1="Copyright  Line 1"  

@contact cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact cn="Contact Name" ph="210-555-1212"   c2="Copyright Line 2" c3="Copyright Line 3" 
@contact cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c3="Copyright Line 3" 
@contact cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2"


@contact  ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact  ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact  ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact  ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c3="Copyright Line 3" 
@contact  ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2"
@contact cn="Contact Name" ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" 
@contact cn="Contact Name" ph="210-555-1212"   c2="Copyright Line 2" c3="Copyright Line 3" 
@contact cn="Contact Name"  em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" 
