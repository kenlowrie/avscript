// Define some useful variables for substitutions

// First get the basic divs
@import '$/divs.md'

// Define a var for underscoring text
@html _id="ul" \
      _inherit="span" \
      style="text-decoration:underline"
@var _id="ul1" \
      _format="{{html.ul.<}}{{self.t}}{{html.ul.>}}" \
      t="TEXT TO UNDERSCORE"

// Define a set of vars for letting me make an ordered list
// This is special, because you have to open the OL, add all the LI and then close the OL
@html _id="ol1" \
      _inherit="ol" \
      style="margin-left:2em"
@var _id="ol1_open" \
     _format="@@ {{html._div_extras_.<}}{{html.ol1.<}}"
@var _id="ol1_close" \
     _format="@@ {{html.ol1.>}}{{html._div_extras_.>}}"

@html _id="li1" \
      _inherit="li" \
      style="font-size:1.3em"

@var _id="li1" \
     _format="@@ {{html.li.<}}{{self.t}}{{html.li.>}}" \
     t="usage: var.li1(t=\"List item\")"

@html _id="comment" \
      _inherit="p" \
      class="note" 

@var _id="comment" \
     _format="{{html.comment.<}}{{self.t}}{{html.comment.>}}" \
     t="usage: var.comment(t=\"your comment here\")"


@html _id="_div_lyrics_" \
      _inherit="div" \
      class="lyrics"
@html _id="_p_lyrics_" \
      _inherit="p" \
      class="lyrics italic"
 
@var _id="lyrics" \
          _format="@@ {{html._div_lyrics_.<}}{{html._p_lyrics_.<}}{{self.t}}[bb]{{self.lyric}}{{html.p.>}}{{html.div.>}}" \
          t="{:.bigandbold}Song Lyrics" \
          lyric="YOUR LYRICS HERE use &#91;b] between lines"

@html _id="_div_scene_" \
      _inherit="div" \
      class="scene"
@html _id="_p_scene_" \
      _inherit="p" \
      class="divTitle"
@html _id="_p_scene_content_" \
      _inherit="p" \
      style="font-size:1.2em" 
 
@var _id="scene" \
          _format="@@ {{html._div_scene_.<}}{{html._p_scene_.<}}{{self.t}}{{html._p_scene_.>}}{{html._div_scene_.>}}" \
          with_content="@@ {{html._div_scene_.<}}{{html._p_scene_.<}}{{self.t}}{{html._p_scene_.>}}{{html._p_scene_content_.<}}{{self.c}}{{html.p.>}}{{html.div.>}}" \
          t="This is your scene title" \
          c="This is your content"

