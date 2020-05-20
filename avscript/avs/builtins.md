//@debug on="ns.add"
[b]=<br />
[bb]=[b][b]
[SP]=&nbsp;
//
@code _id="esc_html"\
      type="eval"\
      src="print('$.url'.replace('<', '&lt;').replace('>','&gt;'))"\
      url="Usage: code.esc_html.run(url=\"text to escape\")"
@code _id="escape2"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.escape_html('$.__t'))"\
      __t="Usage: code.escape.run(t=\"text to escape\")"
@code _id="escape"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.escape_html('$.t'))"\
      t="Usage: code.escape.run(t=\"text to escape\")"
@code _id="encodeURL"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.encodeURL('$.t'))"\
      t="code.encodeURL(t=\"https://www.url to encode.com\")"
@code _id="split_as"\
      type="exec"\
      src="from .utility import CodeHelpers;print(CodeHelpers.split_as('{{self.t}}'))"\
      t="Usage: {{self._}}(t=\"var._public_attrs_\")"
@code _id="pushline"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.pushline('{{self.t}}')"\
      t="Usage: {{self._}}(t=\"line to push onto input stream\")"
@code _id="pushvar"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.pushvar('{{self.t}}')"\
      t="Usage: {{self._}}(t=\"variable whose value will be pushed onto input stream\")"
@code _id="pushlines"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.pushlines('{{self.t}}')"\
      t="Usage: {{self._}}(t=\"lines to push onto input stream. separate lines with \\n \")"
@code _id="datetime_stamp"\
      type="exec"\
      src="from time import strftime;print(strftime(\"{{self.fmtstr}}\"))"\
      _format="{{self.last}}"\
      fmtstr="%Y%m%d @ %H:%M:%S"
@code _id="ln_alias"\
      type="exec"\
      src="from .utility import CodeHelpers;print('@set _id=\"{0}\" \
      {1}=\"{3}{0}.<{4}{2}{3}{0}.>{4}\"'.format('$.nm', \
      '$.attr', '$.lt', CodeHelpers.b(0), CodeHelpers.b(1)))"\
      nm="link.?" attr="_attr_name" lt="NEW_LINK_TEXT_HERE"\
      _help_="<strong><em>usage:</em> \
                {{self._}}</strong>(<em>nm=</em>&quot;link.name_to_add_alias&quot;, \
                <em>attr=</em>&quot;attr_name&quot;, \
                <em>lt=</em>&quot;new link text&quot;)"
@code _id="get"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.get_ns_var('{{self.v}}')"\
      v="variable_name"\
      _help_="Usage: {{self._}}(v=\"variable_name\")"
@code _id="get_default"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.default('$.v', '$.default')"\
      v="default"\
      default="undefined variable"\
      _help_="Usage: {{self._}}(v=&quot;variable_name&quot;, default=&quot;default value&quot;)"
@code _id="repeat"\
      type="eval"\
      src="print('{}'.format('$.t'*$.c))"\
      t="repeat_str "\
      c="2"
@code _id="append"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.append('$._var_', '$._txtvar_')"\
      _var_="_ns.var.attr_"\
      _txtvar_="_ns.txtvar.attr_"\
      _help_="Usage: <strong>{{self._}}(_var_=<em>&quot;ns.var.attr&quot;</em>, _txtvar_=<em>&quot;ns.var.attr with text to add&quot;</em>)</strong>"
@code _id="equals"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.equals('$.v1', '$.v2', '$.true', '$.false')"\
      v1="_ns.var.attr_"\
      v2="_ns.txtvar.attr_"\
      true="_ns.var.true_"\
      false="_ns.var.false_"
@code _id="replace"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.replace('$.var', '$.val', '$.str')"\
      var="varname_to_replace"\
      val="value_to_insert"\
      str="string to operate on"
 
//
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
@html _id="ol" _tag="ol"
@html _id="ul" _tag="ul"
@html _id="li" _tag="li"
@html _id="span" _tag="span"
@html _id="table" _tag="table"
@html _id="th" _tag="th"
@html _id="tr" _tag="tr"
@html _id="td" _tag="td"
@html _id="revision-div" class="revision" _inherit="div"
@html _id="revision-p" class="revTitle" _inherit="p"
@var _id="revision" \
     _format="@@ {{self.inline}}" \
     inline="{{html.revision-div.<}}{{html.revision-p.<}}{{self._v}} {{html.revision-p.>}}{{html.revision-div.>}}" \
     plain="@@ {{self.inline_plain}}"\
     inline_plain="{{html.revision-div.<}}{{html.revision-p.<}}{{self._vp}}{{html.revision-p.>}}{{html.revision-div.>}}" \
     _v="{{self._vp}} ({{code.datetime_stamp.run}})" \
     _vp="Revision: ***{{self.v}}***" \
     v="{{defaults.revision}}"
@html _id="contact-div" class="contact" _tag="div"
@html _id="contact-table" style="border:none" _inherit="table"
@html _id="contact-tr" style="border:none" _inherit="tr"
@html _id="contact-td-left" class="left nowrap" style="border:none" _tag="td"
@html _id="contact-td-right" class="right nowrap" style="border:none" _tag="td"
//
@var _id="contact" \
     _format="@@ {{self.inline}}"\
     inline="{{html.contact-div.<}}{{html.contact-table.<}}{{html.contact-tr.<}}{{html.contact-td-left.<}}{{self.leftside}}{{html.contact-td-left.>}}{{html.contact-td-right.<}}{{self.rightside}}{{html.contact-td-right.>}}{{html.contact-tr.>}}{{html.contact-table.>}}{{html.contact-div.>}}" \
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
     inline="{{self._inline_}}" \
     _inline_="<div class=\"cover\"><h3>{{self.title}}</h3><p>{{self.author}}</p><p class=\"coverSummary\">{{self.logline}}</p></div>"
//
@var _id="cover_template" \
     _inherit="cover" \
     title="{{self.t1}}" \
     author="{{self.t2}}" \
     logline="{{self.t3}}" \
     t1="Title" t2="author" t3="logline"
//
@var _id="cover_factory" \
      _format="@var _id=\"{{self.nm}}\" \
      _inherit=\"cover_template\" \
      t1=\"\" \
      t2=\"{{self.usage}}\" \
      t3=\"\"" \
     usage="Usage:[bb]**{{self.nm}}(t1=&quot;&quot; t2=&quot;text&quot; t3=&quot;&quot;)[b]{{self.nm}}.inline(same)**"
