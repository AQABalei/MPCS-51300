; ModuleID = "prog"
target triple = "x86_64-apple-darwin19.6.0"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

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
  %".13" = bitcast [8 x i8]* @"In If" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13")
  br label %"entry.endif"
entry.else:
  %".16" = bitcast [12 x i8]* @"Not in if" to i8*
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16")
  br label %"entry.endif"
entry.endif:
  ret i32 0
}

@"In If" = internal constant [8 x i8] c"In If \0a\00"
@"Not in if" = internal constant [12 x i8] c"Not in if \0a\00"