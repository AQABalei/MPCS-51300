; ModuleID = "prog"
target triple = "x86_64-apple-darwin19.6.0"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

define i32 @"run"() 
{
entry:
  %".2" = alloca i32
  store i32 -2147483648, i32* %".2"
  %".4" = alloca i32
  store i32 1, i32* %".4"
  %".6" = alloca i32
  %".7" = load i32, i32* %".2"
  %".8" = load i32, i32* %".4"
  %"div" = sdiv i32 %".7", %".8"
  %"eq" = icmp eq i32 %".7", -2147483648
  %"nq" = icmp ne i32 %".8", -1
  %"mul" = mul i1 %"eq", %"nq"
  br i1 %"mul", label %"entry.if", label %"entry.else"
entry.if:
  br label %"entry.endif"
entry.else:
  %"mul.1" = call {i32, i1} @"llvm.smul.with.overflow.i32"(i32 %".7", i32 -1)
  %".11" = extractvalue {i32, i1} %"mul.1", 1
  br i1 %".11", label %"entry.else.if", label %"entry.else.endif"
entry.endif:
  store i32 %"div", i32* %".6"
  %".25" = load i32, i32* %".6"
  %".26" = bitcast [5 x i8]* @"i32" to i8*
  %".27" = call i32 (i8*, ...) @"printf"(i8* %".26", i32 %".25")
  ret i32 0
entry.else.if:
  %".13" = bitcast [31 x i8]* @"Error: cint value overflowed" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13")
  br label %"entry.else.endif"
entry.else.endif:
  %".16" = extractvalue {i32, i1} %"mul.1", 0
  %"mul.2" = call {i32, i1} @"llvm.smul.with.overflow.i32"(i32 %".8", i32 -1)
  %".17" = extractvalue {i32, i1} %"mul.2", 1
  br i1 %".17", label %"entry.else.endif.if", label %"entry.else.endif.endif"
entry.else.endif.if:
  %".19" = bitcast [31 x i8]* @"Error: cint value overflowed" to i8*
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".19")
  br label %"entry.else.endif.endif"
entry.else.endif.endif:
  %".22" = extractvalue {i32, i1} %"mul.2", 0
  br label %"entry.endif"
}

declare {i32, i1} @"llvm.smul.with.overflow.i32"(i32 %".1", i32 %".2") 

@"Error: cint value overflowed" = internal constant [31 x i8] c"Error: cint value overflowed \0a\00"
@"i32" = internal constant [5 x i8] c"%i \0a\00"