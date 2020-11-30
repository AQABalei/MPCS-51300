; ModuleID = "prog"
target triple = "x86_64-apple-darwin19.6.0"
target datalayout = ""

define i32 @"getarg"(i32 %".1") 
{
entry:
  %".3" = alloca i32
  store i32 %".1", i32* %".3"
  %".5" = load i32, i32* %".3"
  %".6" = alloca [0 x i32]
  store [0 x i32] [], [0 x i32]* %".6"
  %".8" = getelementptr [0 x i32], [0 x i32]* %".6", i32 0, i32 %".5"
  %".9" = load i32, i32* %".8"
  ret i32 %".9"
}

define float @"getargf"(i32 %".1") 
{
entry:
  %".3" = alloca i32
  store i32 %".1", i32* %".3"
  %".5" = load i32, i32* %".3"
  %".6" = alloca [0 x float]
  store [0 x float] [], [0 x float]* %".6"
  %".8" = getelementptr [0 x float], [0 x float]* %".6", i32 0, i32 %".5"
  %".9" = load float, float* %".8"
  ret float %".9"
}

declare i32 @"printf"(i8* %".1", ...) 

define i32 @"fib"(i32 %".1") 
{
entry:
  %".3" = alloca i32
  store i32 %".1", i32* %".3"
  %".5" = load i32, i32* %".3"
  %"lt" = icmp slt i32 %".5", 2
  br i1 %"lt", label %"entry.if", label %"entry.endif"
entry.if:
  %".7" = load i32, i32* %".3"
  %"eq" = icmp eq i32 %".7", 0
  br i1 %"eq", label %"entry.if.if", label %"entry.if.else"
entry.endif:
  %".12" = alloca i32
  %".13" = load i32, i32* %".3"
  %"sub" = sub i32 %".13", 1
  %".14" = call i32 @"fib"(i32 %"sub")
  store i32 %".14", i32* %".12"
  %".16" = alloca i32
  %".17" = load i32, i32* %".3"
  %"sub.1" = sub i32 %".17", 2
  %".18" = call i32 @"fib"(i32 %"sub.1")
  store i32 %".18", i32* %".16"
  %".20" = load i32, i32* %".12"
  %".21" = load i32, i32* %".16"
  %"add" = add i32 %".20", %".21"
  ret i32 %"add"
entry.if.if:
  ret i32 0
entry.if.else:
  ret i32 1
}

define void @"inc"(i32* %".1") 
{
entry:
  %".3" = load i32, i32* %".1"
  %"add" = add i32 %".3", 1
  store i32 %"add", i32* %".1"
  ret void
}

define void @"things"(i32* %".1") 
{
entry:
  %".3" = load i32, i32* %".1"
  %"gt" = icmp sgt i32 %".3", 100
  %"logicalNeg" = xor i1 %"gt", -1
  br i1 %"logicalNeg", label %"while_body", label %"while_end"
while_body:
  %".5" = load i32, i32* %".1"
  %".6" = load i32, i32* %".1"
  %"mul" = mul i32 %".5", %".6"
  %"sub" = sub i32 %"mul", 2
  store i32 %"sub", i32* %".1"
  %".8" = load i32, i32* %".1"
  %"gt.1" = icmp sgt i32 %".8", 100
  %"logicalNeg.1" = xor i1 %"gt.1", -1
  br i1 %"logicalNeg.1", label %"while_body", label %"while_end"
while_end:
  ret void
}

define i32 @"run"() 
{
entry:
  %".2" = bitcast [10 x i8]* @"fib(5):" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  %".4" = alloca i32
  %".5" = call i32 @"fib"(i32 5)
  store i32 %".5", i32* %".4"
  %".7" = load i32, i32* %".4"
  %".8" = bitcast [5 x i8]* @"i32" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 %".7")
  %".10" = bitcast [12 x i8]* @"fib(5)+1:" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10")
  call void @"inc"(i32* %".4")
  %".13" = load i32, i32* %".4"
  %".14" = bitcast [5 x i8]* @"i32" to i8*
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i32 %".13")
  %".16" = bitcast [18 x i8]* @"something else:" to i8*
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16")
  call void @"things"(i32* %".4")
  %".19" = load i32, i32* %".4"
  %".20" = bitcast [5 x i8]* @"i32" to i8*
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 %".19")
  ret i32 0
}

@"fib(5):" = internal constant [10 x i8] c"fib(5): \0a\00"
@"i32" = internal constant [5 x i8] c"%i \0a\00"
@"fib(5)+1:" = internal constant [12 x i8] c"fib(5)+1: \0a\00"
@"something else:" = internal constant [18 x i8] c"something else: \0a\00"