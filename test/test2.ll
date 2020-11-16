; ModuleID = "prog"
target triple = "x86_64-apple-darwin19.6.0"
target datalayout = ""

define i32 @"getarg"(i32 %".1") 
{
entry:
  %".3" = alloca [0 x i32]
  %".4" = alloca i32
  store i32 %".1", i32* %".4"
  %".6" = load i32, i32* %".4"
  store [0 x i32] [], [0 x i32]* %".3"
  %".8" = getelementptr [0 x i32], [0 x i32]* %".3", i32 0, i32 %".6"
  %".9" = load i32, i32* %".8"
  ret i32 %".9"
}

define float @"getargf"(i32 %".1") 
{
entry:
  %".3" = alloca [0 x float]
  %".4" = alloca i32
  store i32 %".1", i32* %".4"
  %".6" = load i32, i32* %".4"
  store [0 x float] [], [0 x float]* %".3"
  %".8" = getelementptr [0 x float], [0 x float]* %".3", i32 0, i32 %".6"
  %".9" = load float, float* %".8"
  ret float %".9"
}

declare i32 @"printf"(i8* %".1", ...) 

define float @"test1"(float* %".1", float* %".2", float %".3") 
{
entry:
  %".5" = alloca float
  store float %".3", float* %".5"
  %".7" = alloca i32
  store i32 0, i32* %".7"
  %".9" = alloca i32
  store i32 1, i32* %".9"
  %".11" = alloca i32
  store i32 2, i32* %".11"
  %".13" = load i32, i32* %".11"
  %"gt" = icmp sgt i32 %".13", 8
  br i1 %"gt", label %"w_body", label %"w_after"
w_body:
  %".15" = load float, float* %".1"
  %".16" = load float, float* %".2"
  %"add" = fadd fast float %".15", %".16"
  %".17" = load float, float* %".5"
  %".18" = load float, float* %".1"
  %"div" = fdiv fast float %".17", %".18"
  %".19" = load float, float* %".2"
  %"mul" = fmul fast float %"div", %".19"
  %"sub" = fsub fast float %"add", %"mul"
  %"fptosi" = fptosi float %"sub" to i32
  store i32 %"fptosi", i32* %".7"
  %".21" = load float, float* %".1"
  %".22" = load float, float* %".2"
  %"eq" = fcmp oeq float %".21", %".22"
  br i1 %"eq", label %"w_body.if", label %"w_body.else"
w_after:
  %".43" = load float, float* %".5"
  ret float %".43"
w_body.if:
  store i32 1, i32* %".9"
  br label %"w_body.endif"
w_body.else:
  store i32 0, i32* %".9"
  br label %"w_body.endif"
w_body.endif:
  %".28" = load i32, i32* %".9"
  %"logicalNeg" = xor i32 %".28", -1
  %".29" = load i32, i32* %".11"
  %"gt.1" = icmp sgt i32 %".29", %"logicalNeg"
  %".30" = load float, float* %".1"
  %".31" = load float, float* %".2"
  %"lt" = fcmp olt float %".30", %".31"
  %"and" = and i1 %"gt.1", %"lt"
  %".32" = load float, float* %".5"
  %".33" = load float, float* %".1"
  %"eq.1" = fcmp oeq float %".32", %".33"
  %".34" = load i32, i32* %".7"
  %"eq.2" = icmp eq i32 %".34", 0
  %"or" = or i1 %"eq.1", %"eq.2"
  %"or.1" = or i1 %"and", %"or"
  br i1 %"or.1", label %"w_body.endif.if", label %"w_body.endif.else"
w_body.endif.if:
  %".36" = load float, float* %".1"
  ret float %".36"
w_body.endif.else:
  store float 0x4021000000000000, float* %".1"
  br label %"w_body.endif.endif"
w_body.endif.endif:
  store float 0x401cccccc0000000, float* %".2"
  %".41" = load i32, i32* %".11"
  %"gt.2" = icmp sgt i32 %".41", 8
  br i1 %"gt.2", label %"w_body", label %"w_after"
}

define i32 @"run"() 
{
entry:
  %".2" = alloca float
  %".3" = call float @"getargf"(i32 0)
  store float %".3", float* %".2"
  %".5" = alloca float
  %".6" = call float @"getargf"(i32 1)
  store float %".6", float* %".5"
  %".8" = alloca float
  %".9" = call float @"getargf"(i32 2)
  store float %".9", float* %".8"
  %".11" = bitcast [11 x i8]* @"initial:" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11")
  %".13" = load float, float* %".2"
  %".14" = fpext float %".13" to double
  %".15" = bitcast [5 x i8]* @"double" to i8*
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", double %".14")
  %".17" = load float, float* %".5"
  %".18" = fpext float %".17" to double
  %".19" = bitcast [5 x i8]* @"double" to i8*
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".19", double %".18")
  %".21" = load float, float* %".8"
  %".22" = fpext float %".21" to double
  %".23" = bitcast [5 x i8]* @"double" to i8*
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".23", double %".22")
  %".25" = load float, float* %".8"
  %".26" = call float @"test1"(float* %".2", float* %".5", float %".25")
  %".27" = bitcast [9 x i8]* @"final:" to i8*
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".27")
  %".29" = load float, float* %".2"
  %".30" = fpext float %".29" to double
  %".31" = bitcast [5 x i8]* @"double" to i8*
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".31", double %".30")
  %".33" = load float, float* %".5"
  %".34" = fpext float %".33" to double
  %".35" = bitcast [5 x i8]* @"double" to i8*
  %".36" = call i32 (i8*, ...) @"printf"(i8* %".35", double %".34")
  %".37" = load float, float* %".8"
  %".38" = fpext float %".37" to double
  %".39" = bitcast [5 x i8]* @"double" to i8*
  %".40" = call i32 (i8*, ...) @"printf"(i8* %".39", double %".38")
  ret i32 0
}

@"initial:" = internal constant [11 x i8] c"initial: \0a\00"
@"double" = internal constant [5 x i8] c"%f \0a\00"
@"final:" = internal constant [9 x i8] c"final: \0a\00"