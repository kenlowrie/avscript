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
[cls]:https://www.cloudylogic.com
- Shot - [cls] <-- should be a link to www.cloudylogic.com
    Shot 2 - [cls]
    {:.red}Shot 3 - [cls]
    Shot 4 - [cls] - Working good..
Description
[Google]:(https://www.google.com)
- Shot - [Google] <-- Should be link to google.com
Description
[amazon]:https://www.amazon.com "amazon website"
- Shot - [amazon] <-- Should be link to amazon.com with title "amazon website"
Description
[Amazon]:https://www.amazon.com "Amazon website"
- Shot - [Amazon] <-- Should be link to amazon.com with title "Amazon website"
Description
//$$revision$$:<<1b>>
- Shot
Description
$$cover$$:<<A>>:<<B>>:<<C>>
- Shot
Description
$$contact$$:<<A>>:<<B>>:<<C>>:<<D>>:<<E>>:<<F>>
- Shot
Description
// ///Variables///
- Shot
Description
// ///Links///
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
@+[myanchor]
@:[myanchor]<<*This is my text*>>

