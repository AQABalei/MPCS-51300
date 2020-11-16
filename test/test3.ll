; ModuleID = "prog"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

declare void @"printString"(i8* %".1") 

declare void @"printInt"(i32 %".1") 

declare void @"printFloat"(float %".1") 

define i32 @"run"() 
{
entry:
  %".2" = alloca float
  store float 0x4000000000000000, float* %".2"
  %".4" = alloca float
  store float 0x3ff8000000000000, float* %".4"
  %".6" = alloca float
  store float 0x400d9999a0000000, float* %".6"
  %".8" = load float, float* %".2"
  %".9" = load float, float* %".4"
  %"gt" = fcmp ogt float %".8", %".9"
  %".10" = load float, float* %".4"
  %".11" = load float, float* %".6"
  %"lt" = fcmp olt float %".10", %".11"
  %"and" = and i1 %"gt", %"lt"
  br i1 %"and", label %"entry.if", label %"entry.else"
entry.if:
  %".13" = bitcast [5 x i8]* @"In If" to i8*
  call void @"printString"(i8* %".13")
  br label %"entry.endif"
entry.else:
  %".16" = bitcast [9 x i8]* @"Not in if" to i8*
  call void @"printString"(i8* %".16")
  br label %"entry.endif"
entry.endif:
  ret i32 0
}

@"In If" = constant [5 x i8] c"In If"
@"Not in if" = constant [9 x i8] c"Not in if"