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
  %".5" = icmp eq i32 1, -2147483648
  br i1 %".5", label %"entry.if", label %"entry.endif"
entry.if:
  %".7" = bitcast [31 x i8]* @"Error: cint value overflowed" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7")
  br label %"entry.endif"
entry.endif:
  %"Minus" = sub i32 0, 1
  store i32 %"Minus", i32* %".4"
  %".11" = alloca i32
  %".12" = load i32, i32* %".2"
  %".13" = load i32, i32* %".4"
  %"eq" = icmp eq i32 %".12", -2147483648
  %"eq.1" = icmp eq i32 %".13", -1
  %"eq.2" = icmp eq i32 %".13", 0
  %"and" = and i1 %"eq", %"eq.1"
  %"or" = or i1 %"and", %"eq.2"
  br i1 %"or", label %"entry.endif.if", label %"entry.endif.endif"
entry.endif.if:
  %".15" = bitcast [31 x i8]* @"Error: cint value overflowed" to i8*
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15")
  br label %"entry.endif.endif"
entry.endif.endif:
  %"div" = sdiv i32 %".12", %".13"
  store i32 %"div", i32* %".11"
  %".19" = load i32, i32* %".11"
  %".20" = bitcast [5 x i8]* @"i32" to i8*
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 %".19")
  ret i32 0
}

@"Error: cint value overflowed" = internal constant [31 x i8] c"Error: cint value overflowed \0a\00"
@"i32" = internal constant [5 x i8] c"%i \0a\00"