from langchain_community.tools import DuckDuckGoSearchRun,ShellTool

#1
search_tool=DuckDuckGoSearchRun()
result1=search_tool.invoke('ipl news')
print(result1)


#2
shell_tool= ShellTool()
result2=shell_tool.invoke('whoami')
print(result2)

