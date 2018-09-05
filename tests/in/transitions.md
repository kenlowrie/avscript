{:.red.center}### avscript tester doc
{:.blue.plain}--- plainTitle Transitions
    This test document is used to test the transitions from A/V sections
- Shot
Description
- Shot
Description
{:.plain}--- plainTitle This should be a new section
- Shot
Description
{:.green.plain}@@@ plainTitle This should be a new section
- Shot
Description
[variable]=VALUE
- Shot - [variable] <-- should be the word VALUE
Description
- Shot
Description
@link _="cls" _inherit="_template_" href="https://www.cloudylogic.com" _text="{{self._}}"
- Shot - [cls] <-- should be a link to www.cloudylogic.com
    Shot 2 - [cls]
    {:.red}Shot 3 - [cls]
    Shot 4 - [cls] - Working good..
Description
@link _="Google" _inherit="_template_" href="https://www.google.com" _text="{{self._}}"
- Shot - [Google] <-- Should be link to google.com
Description
@link _="amazon" _inherit="_template_" title="amazon website" href="https://www.amazon.com" _text="{{self._}}"
- Shot - [amazon] <-- Should be link to amazon.com with title "amazon website"
Description
@link _="Amazon" _inherit="_template_" title="Amazon website" href="https://www.amazon.com" _text="{{self._}}"
- Shot - [Amazon] <-- Should be link to amazon.com with title "Amazon website"
Description
//$$revision$$:<<1b>>
- Shot
Description
@@ [var.cover(title="A" author="B" logline="C")]
- Shot
Description
@@ [var.contact(c1="D" c2="E"  c3="F"  cn = "A"  ph  =  "B"    em   ="C")]
- Shot
Description
@dump basic="b|v" var="cover"

- Shot
Description
@dump link="A|G|a|c"
- Shot
Description
///Shotlist///
- Shot
Description
# Header
- Shot
Description
{:.red}##Header2a
- Shot
Description
{:.red}$$revision$$:<<1 This should not be a new div, class prefixes are not allowed here.>>
{:.blue}$$cover$$:<<.NOT>>:<<.HERE>>:<<.EITHER>>
{:.green}$$contact$$:<<.NOT>>:<<.HERE>>:<<.EITHER>>:<<1>>:<<2>>:<<3>>
{:.red}[variable]=NO NOT HERE EITHER
{:.blue}[link]:not_in_links_either_
@break
[link.bm_factory(nm="myanchor" t="*This is my text*")]
[link.myanchor]
[link.myanchor.link]

