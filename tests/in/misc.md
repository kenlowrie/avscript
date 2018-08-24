//Add tests here that don't fit elsewhere (or I'm too lazy to look)
//
[var]={:.red}This text will be RED
Example: [var]
[SP]=&nbsp;

{:.syntax}--- divTitle Variable Decorators
    [SP]
    {:.bigandbold.indent}&#91;variable]={:.class}value

So, if you declared this: &#91;mynewvar]={:.bigandbold.red}My new big bold value, and then put &#91;mynewvar], you'd get this:
[mynewvar]={:.bigandbold.red}My new big bold value
[mynewvar]

[title]=Production Estimate

// Define some useful variables for substitions
[newsect]=<div class="pbb plain left"><p class="plainTitle">[SECTION]</p></div>
[dcp]=<div class="plain left">
[/div]=</div>
[pc1]=<p class="plainTitle">
[/p]=</p>
[inlinesect]=[dcp][pc1][SECTION][/p][/div]
[li]=<li style="font-size:1.3em">
[/li]=</li>
[ol]=<div class="extras"><ol style="margin-left:2em">
[/ol]=</ol></div>
[break]=<br />
[dblbrk]=[break][break]
[UL]=<span style="text-decoration:underline">
[/UL]=</span>

[you@yourdomain.com]=__DELETEME__mailto:you@youremailaddress.com
[FancyMe]={:.bigandbold}Firstname LastName
[phone]=512.867.5309
[sigme]=[FancyMe]<br />Producer<br />Production Company<br />[phone]<br />[you@yourdomain.com]
[signature]=<br /><div class="extras"><p>[sigme]</p></div>

[SECTION]=[title]
@raw [newsect]

{:.syntax.width90}--- divTitle Specifics when choosing TRT option
    [break]
    {:.indent2}This rate applies to editing normal footage (video, photos, audio). As an example, the demo film that we produced would have all fit under this rate, with one exception (green screen footage that was keyed for ending). However, if we are given footage that requires *specialized attention*, a different rate will apply on a per clip basis.[dblbrk]
    {:.indent2}Some examples that require specialized attention are: Footage that is shot on green screen and must be keyed. Footage that is shaky and must be stabilized. Footage shot with incorrect color temperature. Any media (video/photos) that requires rotoscoping. Audio that must be cleaned up.

1. [UL]**Per hour**[/UL]. Editing for this project will be billed at $60/hr. Since we bill based upon hours spent, there are no exceptions to the type of footage being edited, as is the case with the ***"Per runtime minute of film"*** estimate above.

2. [UL]**Per project**[/UL]. An estimate for the entire project requires a completed script in AV format, with all details ironed out, including exact clips to be used, footage to be shot, etc. Given those requirements, it is not feasible to provide this option for consideration at this time.

For this project, only billing options 1 and 2 will be offered.

[SECTION]=Retainer
@raw [inlinesect]

If you decide to hire [Cloudy Logic Studios] for this project, no retainer will be required.

[SECTION]=Invoicing
@raw [inlinesect]

Once the project is underway, we will invoice periodically as various milestones are met. These milestones will be set and agreed upon by both parties prior to commencement. They will be something like this:

@raw [ol]
@raw [li]Rough cut *- might be in stages*[/li]
@raw [li]Picture lock *- no changes to timeline after this*[/li]
@raw [li]Color grade complete *- possible after audio mixing*[/li]
@raw [li]Audio mixing complete *- possible before color grade*[/li]
@raw [li]Film completion[/li]
@raw [/ol]

If the project is being billed per runtime minute, the milestone invoices will be billed in fractional estimates of the minimum runtime up until picture lock, at which time remaining invoices will be billed based on the actual total runtime.

If the project is being billed per hour, then invoices at each milestone will reflect the total based on hours invested to achieve the milestone.

Usually, work on the next milestone will not commence until the invoice for the prior milestone has been paid.

Finally, keep in mind that final media will not be released until all invoices are paid in full.

[SECTION]=Summary
@raw [inlinesect]

If you would like to move forward with the project, here are the [UL]**next steps**[/UL]:

@raw [ol]
@raw [li]Choose a billing option[/li]
@raw [li]Iron out milestones[/li]
@raw [li]Acceptance of Terms - return signed contract[/li]
@raw [/ol]

Thanks again for choosing us for your production needs. We look forward to working with you on this project. 

Please let [me] know if you have any questions regarding this estimate, or if you need any clarifications and/or changes.

Warmest regards,
@raw [signature]

{:.pbb}## [UL]Terms and Signatures[/UL]

If you agree to the terms and conditions outlined in this proposal, select a billing option, [UL]initial each page[/UL], sign/print/date below, and return the entire contract to [info@cloudylogic.com].

[option1]={:.bigandbold}[SP][SP]{[SP][SP]} Per runtime minute.
[option2]={:.bigandbold}[SP][SP]{[SP][SP]} Per hour.

**Choose your Billing Option**: [dblbrk][option1][break][option2] 

Upon final acceptance of video, an invoice will be generated outlining the final amount due. Payment is due within 30 days of final acceptance.

{:.note.bigandbold}**NOTE**: Final media is [UL]*not delivered*[/UL] until all outstanding invoices have been paid in full.
[dblbrk]
### [UL]Signatures[/UL]
