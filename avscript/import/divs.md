// Variables that abstract the different types of DIVs
@html _id="_div_extras_" \
      _inherit="div" \
      class="extras"

@html _id="_div_section_" \
      _inherit="div" \
      class="section"
@html _id="_div_section_pbb_" \
      _inherit="_div_section_" \
      class="section pbb"
@html _id="_p_section_" \
      _inherit="p" \
      class="divTitle"
@html _id="_p_section_content_" \
      _inherit="p" \
      style="font-size:1.2em" 
 
@var _id="section" \
          _format="@@ {{html._div_section_.<}}{{html._p_section_.<}}{{self.t}}{{html._p_section_.>}}{{html._div_section_.>}}" \
          with_content="@@ {{html._div_section_.<}}{{html._p_section_.<}}{{self.t}}{{html._p_section_.>}}{{html._p_section_content_.<}}{{self.c}}{{html.p.>}}{{html.div.>}}" \
          t="This is your section title" \
          c=""
@var _id="section_pbb" \
          _inherit="section" \ 
          _format="@@ {{html._div_section_pbb_.<}}{{html._p_section_.<}}{{self.t}}{{html._p_section_.>}}{{html._div_section_.>}}" \
          with_content="@@ {{html._div_section_pbb_.<}}{{html._p_section_.<}}{{self.t}}{{html._p_section_.>}}{{html._p_section_content_.<}}{{self.c}}{{html.p.>}}{{html.div.>}}" \

@html _id="_div_plain_" \
      _inherit="div" \
      class="plain"
@html _id="_p_plain_" \
      _inherit="p" \
      class="plainTitle"
@html _id="_p_plain_content_" \
      _inherit="p" \
      style="font-size:1.2em" 
 
@var _id="plain" \
          _format="@@ {{html._div_plain_.<}}{{html._p_plain_.<}}{{self.t}}{{html._p_plain_.>}}{{html._div_plain_.>}}" \
          with_content="@@ {{html._div_plain_.<}}{{html._p_plain_.<}}{{self.t}}{{html._p_plain_.>}}{{html._p_plain_content_.<}}{{self.c}}{{html.p.>}}{{html.div.>}}" \
          t="This is your plain title" \
          c="This is your plain content"
