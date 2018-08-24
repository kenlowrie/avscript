// Test script for varv2 support
[b]=<br />
@var _noid="noid"
@var id="alsonoid"
@var _id="id0" attr1="attribute 1"
@var _="id1" attr1="attribute 1"
[id0]
[id0.attr1]
[varv2.id0]
[varv2.id0.attr1]
id0._id=[id0._id][b]id0.__=[id0.__][b]id0._=[id0._][b]id0.name=[id0.name]
[varv2]
[varv2.]
[varv2.nothing]
///Variables///

@set foo="bar"
@set _id="id1" attr1="New Value"
ATTR1 should be "New Value":
[id1]
# ------------------------
@set _id="id1" foo="bar"
[id1]
@set _id="id1" foo="nubar" bar="oldfu"
[id1]
@set _id="id2" foo="nubar" bar="oldfu"
[id2]
@var __="id2" 1="1" 2="2" 3="3" 4="4" 5="5" 6="6" 7="7" 8="8" 9="9" 10="10"\
               11="11" 12="12" 13="13" 14="14" 15="15" 16="16" 17="17" 18="18" 19="19" 20="20" 21="21"
[id2]
@set _id="id2" 1="x1" 2="x2" 3="x3" 4="x4" 5="x5" 6="x6" 7="x7" 8="x8" 9="x9" 10="x10"\
               11="x11" 12="x12" 13="x13" 14="x14" 15="x15" 16="x16" 17="x17" 18="x18" 19="x19" 20="x20" 21="x21"

[id2]

///Variables///
