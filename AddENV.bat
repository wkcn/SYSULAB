::检查path中有没有%1(有就跳到run，没有就接着执行)
rem echo off
echo %path%|findstr /i "%1"&&(goto eof)
 
::先添加，防止没有时修改出错
wmic ENVIRONMENT create name="path",VariableValue="%1;%path%"
::再修改，防止已有时添加出错
wmic ENVIRONMENT where "name='path' and username='<system>'" set VariableValue="%1;%path%"
::再即时应用
set "path=%1;%path%"
 
:eof
