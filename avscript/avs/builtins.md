[b]=<br />
[bb]=[b][b]
    
[SP]=&nbsp;
@code _id="esc_html"\
      type="eval"\
      src="print('{{self.url}}'.replace('<', '&lt;').replace('>','&gt;'))"\
      url="Usage: code.esc_html(url=\"text to escape\")"
@code _id="datetime_stamp"\
      type="exec"\
      src="from time import strftime;print(strftime(\"{{self.fmtstr}}\"))"\
      _format="{{self.last}}"\
      fmtstr="%Y%m%d @ %H:%M:%S"
@var _id="defaults"\
     title="[title]"\
     author="[author]"\
     logline="[logline]"\
     _nop=""
@link _id="_template_" \
      _format="{{self.<}}{{self._text}}{{self.>}}" \
      _text="Usage: link.{{self._}}(_text=\"Text to Link\")" \
      href="www.YOUR-URL-GOES-HERE.com" \
      _asurl="{{self.<}}{{code.esc_html.run(url=\"{{self.href}}\")}}{{self.>}}" \
      _qlink="{{self.<}}{{self._qtext}}{{self.>}}" \
      _qtext="SETMETOLINKTEXT"
@link _id="ln_factory" \
      _format="@link _id=\"{{self.nm}}\" _inherit=\"_template_\" href=\"{{self.hr}}\" \
      _text=\"{{self.t}}\""
@link _id="bm_template" \
      id="{{self._}}" \
      _format="@@ {{self._inline}}" \
      link="<a href=\"#{{self.id}}\">{{self.text}}</a>" \
      text="TEXT-TO-DISPLAY-FOR-LINK"   \
      _inline="<a id=\"{{self.id}}\"></a>"
@link _id="bm_factory" \
      _format="@link _id=\"{{self.nm}}\" _inherit=\"bm_template\" text=\"{{self.t}}\""
@html _id="div" _tag="div"
@html _id="p" _tag="p"
@html _id="table" _tag="table"
@html _id="th" _tag="th"
@html _id="tr" _tag="tr"
@html _id="td" _tag="td"
@html _id="revision-div" class="revision" _inherit="div"
@html _id="revision-p" class="revTitle" _inherit="p"
@var _id="revision" \
     _format="@@ {{self._inline_}}" \
     _inline_="{{html.revision-div.<}}{{html.revision-p.<}}{{self.v}} {{html.revision-p.>}}{{html.revision-div.>}}" \
     plain="@@ {{self._inline_plain_}}"\
     _inline_plain_="{{html.revision-div.<}}{{html.revision-p.<}}{{self.vp}}{{html.revision-p.>}}{{html.revision-div.>}}" \
     v="{{self.vp}} ({{code.datetime_stamp.run}})" \
     vp="Revision: ***[self.revision]***" \
     revision="{{defaults.revision}}"
@html _id="contact-div" class="contact" _tag="div"
@html _id="contact-table" style="border:none" _inherit="table"
@html _id="contact-tr" style="border:none" _inherit="tr"
@html _id="contact-td-left" class="left nowrap" style="border:none" _tag="td"
@html _id="contact-td-right" class="right nowrap" style="border:none" _tag="td"
//
@var _id="contact" \
     _format="@@ {{self._inline_}}"\
     _inline_="{{html.contact-div.<}}{{html.contact-table.<}}{{html.contact-tr.<}}{{html.contact-td-left.<}}{{self.leftside}}{{html.contact-td-left.>}}{{html.contact-td-right.<}}{{self.rightside}}{{html.contact-td-right.>}}{{html.contact-tr.>}}{{html.contact-table.>}}{{html.contact-div.>}}" \
     rightside="{{self.cn}}<br />{{self.ph}}<br />{{self.em}}<br />" \
     leftside="{{self.c1}}<br />{{self.c2}}<br />{{self.c3}}<br />" \
     cn="{{defaults.cn}}" \
     ph="{{defaults.ph}}" \
     em="{{defaults.em}}" \
     c1="{{defaults.c1}}" \
     c2="{{defaults.c2}}" \
     c3="{{defaults.c3}}"
//
@var _id="cover"\
     title="{{defaults.title}}" \
     author="{{defaults.author}}" \
     logline="{{defaults.logline}}" \
     _format="@@ {{self._inline_}}" \
     _inline_="<div class=\"cover\"><h3>{{self.title}}</h3><p>{{self.author}}</p><p class=\"coverSummary\">{{self.logline}}</p></div>"
//
@var _id="cover_template" \
     _inherit="cover" \
     title="{{self.t1}}" \
     author="{{self.t2}}" \
     logline="{{self.t3}}" \
     t1="Title" t2="author" t3="logline" \
     _format="@@ {{self._inline_}}" \
     inline="{{self._inline_}}"
//
@var _id="cover_factory" \
      _format="@var _id=\"{{self.nm}}\" \
      _inherit=\"cover_template\" \
      t1=\"\" \
      t2=\"{{self.usage}}\" \
      t3=\"\"" \
     usage="Usage: **{{self.nm}}(t2=&quot;text&quot;)** or **{{self.nm}}.gencover(t2=&quot;text&quot;**)"
