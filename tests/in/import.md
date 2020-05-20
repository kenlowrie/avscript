{:.blue}#AVScript User Manual
[workingtitle]=AVScript&#32;Markdown&#32;Utility
[storysummary]=This manual describes the *AVScript Markdown Utility*, its features, purpose and more. I've packed it with examples too, so hopefully after you read it, you'll know all you need to know about how to use it to create A/V Style scripts quickly, easily and most important, efficiently. ***Enjoy!***
@var _id="_path_" path="/Users/ken/Dropbox/shared/src/script/avscript/tests/in/import" _format="{{self.path}}"
@import '[var._path_(path="in/import/")]/test_import.md'
[SP]=&nbsp;
[a]=testing
[b]=123
[c]=[{{a}}][{{b}}]
And here's my test: [a][b] and finally [c]

@import '[var._path_]/test_import2.md'

@dump basic=".*" var=".*" link="c|d"
