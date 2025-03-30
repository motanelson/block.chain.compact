program pt;

uses
   sysutils,classes,dateutils,crt,process,StrUtils;
 
    
var i : integer;
    f : text;
    c : Char;
    s : ansistring;
    ss : String;
    sss : String;
    Processs: TProcess;
    Processs2: TProcess;
begin
  Processs := TProcess.Create(nil);
  Processs.InheritHandles := False;
  Processs.Options := [];
  Processs.ShowWindow := swoShow;
  Processs2 := TProcess.Create(nil);
  Processs2.InheritHandles := False;
  Processs2.Options := [];
  Processs2.ShowWindow := swoShow;
  c:=char(27);
  ss:='';
  sss:='';
  s:='';
  writeln (c+'c'+c+'[43;30mgive a text file',s);
  readln(ss);
  sss:=copy(ss,1);
  sss:=replacestr(ss,'.txt','.ps');
  processs.commandline :='enscript '+ss+' --output='+sss ;
  processs.execute;
  processs.free;
  processs2.commandline :='ps2pdf '+sss ;
  processs2.execute;
  processs2.free;
  
end.
