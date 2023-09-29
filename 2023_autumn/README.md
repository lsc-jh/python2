# 2023 Autumn Python 2

### Extra tools used

For generating the recursion diagrams we had to install the following pip packages:
- `py -m "pip" install recursion-visualiser`
- `py -m "pip" install graphviz`

And download the following zip: [Graphviz download](https://www2.graphviz.org/Packages/stable/windows/10/msbuild/Release/Win32/graphviz-2.44.1-win32.zip)

Set up graphviz with the following command:
```ps1

Invoke-WebRequest -Uri "https://www2.graphviz.org/Packages/stable/windows/10/msbuild/Release/Win32/graphviz-2.44.1-win32.zip" -OutFile "C:\graph.zip"; Expand-Archive -Path "C:\graph.zip" -DestinationPath "C:\tools\graph\"

```
