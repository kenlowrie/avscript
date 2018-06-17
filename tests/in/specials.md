@+[special+sections]
##Cover, Revision & Contact Sections

There are three (3) specialized sections that can be defined within your document to add commonly used information in script files. They are:

{:.indent}###$$cover$$ - To add a cover section
{:.indent}###$$revision$$ - To add a revision section
{:.indent}###$$contact$$ - To add a contact section

The details for each type of section are as follows:

###$$cover$$&lt;&lt;title of script&gt;&gt;:&lt;&lt;short summary&gt;&gt;:&lt;&lt;long description&gt;&gt;

Each element within the ***&lt;&lt;[SP]&gt;&gt;*** is optional. The ***&lt;&lt;[SP]&gt;&gt;*** are required, even if you don't want to specify the element!


###$$revision$$&lt;&lt;revision of script&gt;&gt;
Specify the revision number of your document within the angle brackets. Note that the current date and time of the document at the time of processing will also be inserted immediately following the revision number. This provides additional clarification of the version, in case you forget to bump the version number.

###$$contact$$&lt;&lt;contact name&gt;&gt;:&lt;&lt;contact phone&gt;&gt;:&lt;&lt;contact email&gt;&gt;:&lt;&lt;copyright statement 1&gt;&gt;:&lt;&lt;copyright statement 2&gt;&gt;:&lt;&lt;copyright statement 3&gt;&gt;

Each element within the ***&lt;&lt;[SP]&gt;&gt;*** is optional. The ***&lt;&lt;[SP]&gt;&gt;*** are required, even if you don't want to specify the element! 

To see these tags in action, take a look at the userguideheading.md document in the import folder of this user guide.

// And now let's try various versions
$$cover$$:
$$cover$$:<<>>
$$cover$$:<<>>:<<>>
$$cover$$:<<>>:<<>>:<<>>
$$cover$$:<<Title of Script>>:<<>>:<<>>
$$cover$$:<<Title of Script>>:<<Script Author>>:<<>>
$$cover$$:<<Title of Script>>:<<Script Author>>:<<Log Line>>
$$cover$$:<<>>:<<Script Author>>:<<>>
$$cover$$:<<>>:<<>>:<<Log Line>>
$$cover$$:<<>>:<<Script Author>>:<<Log Line>>
$$cover$$:<<Title of Script>>:<<>>:<<Log Line>>
$$cover$$:<<Title of Script>>
$$cover$$:<<Title of Script>>:<<Script Author>>
$$cover$$:<<>>:<<Script Author>>


$$contact$$:
$$contact$$:<<>>
$$contact$$:<<>>:<<>>
$$contact$$:<<>>:<<>>:<<>>
$$contact$$:<<>>:<<>>:<<>>:<<>>
$$contact$$:<<>>:<<>>:<<>>:<<>>:<<>>
$$contact$$:<<>>:<<>>:<<>>:<<>>:<<>>:<<>>
$$contact$$:<<Contact Name>>:<<>>:<<>>:<<>>:<<>>:<<>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<>>:<<>>:<<>>:<<>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<email>>:<<>>:<<>>:<<>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<>>:<<>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<Copyright Line 3>>

$$contact$$:<<Contact Names>>
$$contact$$:<<Contact Name>>:<<Phones>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<emails>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAMES, LLC.>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All My Rights Reserved.>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<Copyright Line 3>>

$$contact$$:<<>>:<<Phone>>:<<>>:<<>>:<<>>:<<>>
$$contact$$:<<>>:<<Phone>>:<<email>>:<<>>:<<>>:<<>>
$$contact$$:<<>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAMEX, LLC.>>
$$contact$$:<<>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<>>
$$contact$$:<<>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<Copyright Line 3>>

$$contact$$:<<>>:<<>>:<<email>>:<<>>:<<>>:<<>>
$$contact$$:<<>>:<<>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<>>:<<>>
$$contact$$:<<>>:<<>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<>>
$$contact$$:<<>>:<<>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<Copyright Line 3>>

$$contact$$:<<>>:<<>>:<<>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<>>:<<>>
$$contact$$:<<>>:<<>>:<<>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<>>
$$contact$$:<<>>:<<>>:<<>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<Copyright Line 3>>

$$contact$$:<<>>:<<>>:<<>>:<<>>:<<All Rights Reserved.>>:<<>>
$$contact$$:<<>>:<<>>:<<>>:<<>>:<<All Rights Reserved.>>:<<Copyright Line 3>>

$$contact$$:<<>>:<<>>:<<>>:<<>>:<<>>:<<Copyright Line 3>>

$$contact$$:<<>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<email>>:<<>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<>>

$$contact$$:<<>>:<<>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<>>:<<Phone>>:<<>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<>>:<<Phone>>:<<email>>:<<>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<>>:<<Copyright Line 3>>
$$contact$$:<<>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<>>


$$contact$$:<<Contact Name>>:<<>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<>>:<<>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<>>:<<email>>:<<>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<>>

$$contact$$:<<Contact Name>>:<<Phone>>:<<>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<>>:<<>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<>>

$$contact$$:<<Contact Name>>:<<Phone>>:<<email>>:<<>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<email>>:<<>>:<<>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<email>>:<<>>:<<All Rights Reserved.>>:<<>>

$$contact$$:<<Contact Name>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<>>:<<>>

$$contact$$:<<Contact Name>>:<<>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<>>:<<>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<>>:<<>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<>>:<<>>

$$contact$$:<<Contact Name>>:<<Phone>>:<<>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<>>:<<>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<>>


$$contact$$:<<>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<>>:<<Phone>>:<<>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<>>:<<Phone>>:<<email>>:<<>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<>>:<<Copyright Line 3>>
$$contact$$:<<>>:<<Phone>>:<<email>>:<<Copyright (c) 2018 by YOURNAME, LLC.>>:<<All Rights Reserved.>>:<<>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<email>>:<<>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<Phone>>:<<>>:<<>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
$$contact$$:<<Contact Name>>:<<>>:<<email>>:<<>>:<<All Rights Reserved.>>:<<Copyright Line 3>>
