/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison implementation for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "3.0.4"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1




/* Copy the first part of user declarations.  */
#line 1 "rmgrm.y" /* yacc.c:339  */


#include <stdio.h>
#include "rnamot.h"

extern	VALUE_T	rm_tokval;
extern	int	rm_context;

extern	void	RM_hold(NODE_T *);
extern	void	RM_release(NODE_T *);

/*
typedef	union	{
	int	ival;
	NODE_T	*npval;
} YYSTYPE;
*/


#line 86 "y.tab.c" /* yacc.c:339  */

# ifndef YY_NULLPTR
#  if defined __cplusplus && 201103L <= __cplusplus
#   define YY_NULLPTR nullptr
#  else
#   define YY_NULLPTR 0
#  endif
# endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* In a future release of Bison, this section will be replaced
   by #include "y.tab.h".  */
#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 1
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    SYM_PARMS = 258,
    SYM_DESCR = 259,
    SYM_SITES = 260,
    SYM_SCORE = 261,
    SYM_SE = 262,
    SYM_CTX = 263,
    SYM_SS = 264,
    SYM_H5 = 265,
    SYM_H3 = 266,
    SYM_P5 = 267,
    SYM_P3 = 268,
    SYM_T1 = 269,
    SYM_T2 = 270,
    SYM_T3 = 271,
    SYM_Q1 = 272,
    SYM_Q2 = 273,
    SYM_Q3 = 274,
    SYM_Q4 = 275,
    SYM_ACCEPT = 276,
    SYM_BEGIN = 277,
    SYM_BREAK = 278,
    SYM_CONTINUE = 279,
    SYM_ELSE = 280,
    SYM_END = 281,
    SYM_FOR = 282,
    SYM_HOLD = 283,
    SYM_IF = 284,
    SYM_IN = 285,
    SYM_REJECT = 286,
    SYM_RELEASE = 287,
    SYM_WHILE = 288,
    SYM_IDENT = 289,
    SYM_INT = 290,
    SYM_FLOAT = 291,
    SYM_STRING = 292,
    SYM_PAIRSET = 293,
    SYM_AND = 294,
    SYM_ASSIGN = 295,
    SYM_DOLLAR = 296,
    SYM_DONT_MATCH = 297,
    SYM_EQUAL = 298,
    SYM_GREATER = 299,
    SYM_GREATER_EQUAL = 300,
    SYM_LESS = 301,
    SYM_LESS_EQUAL = 302,
    SYM_MATCH = 303,
    SYM_MINUS = 304,
    SYM_MINUS_ASSIGN = 305,
    SYM_MINUS_MINUS = 306,
    SYM_NEGATE = 307,
    SYM_NOT = 308,
    SYM_NOT_EQUAL = 309,
    SYM_OR = 310,
    SYM_PERCENT = 311,
    SYM_PERCENT_ASSIGN = 312,
    SYM_PLUS = 313,
    SYM_PLUS_ASSIGN = 314,
    SYM_PLUS_PLUS = 315,
    SYM_STAR = 316,
    SYM_STAR_ASSIGN = 317,
    SYM_SLASH = 318,
    SYM_SLASH_ASSIGN = 319,
    SYM_LPAREN = 320,
    SYM_RPAREN = 321,
    SYM_LBRACK = 322,
    SYM_RBRACK = 323,
    SYM_LCURLY = 324,
    SYM_RCURLY = 325,
    SYM_COLON = 326,
    SYM_COMMA = 327,
    SYM_SEMICOLON = 328,
    SYM_CALL = 329,
    SYM_LIST = 330,
    SYM_KW_STREF = 331,
    SYM_IX_STREF = 332,
    SYM_ERROR = 333
  };
#endif
/* Tokens.  */
#define SYM_PARMS 258
#define SYM_DESCR 259
#define SYM_SITES 260
#define SYM_SCORE 261
#define SYM_SE 262
#define SYM_CTX 263
#define SYM_SS 264
#define SYM_H5 265
#define SYM_H3 266
#define SYM_P5 267
#define SYM_P3 268
#define SYM_T1 269
#define SYM_T2 270
#define SYM_T3 271
#define SYM_Q1 272
#define SYM_Q2 273
#define SYM_Q3 274
#define SYM_Q4 275
#define SYM_ACCEPT 276
#define SYM_BEGIN 277
#define SYM_BREAK 278
#define SYM_CONTINUE 279
#define SYM_ELSE 280
#define SYM_END 281
#define SYM_FOR 282
#define SYM_HOLD 283
#define SYM_IF 284
#define SYM_IN 285
#define SYM_REJECT 286
#define SYM_RELEASE 287
#define SYM_WHILE 288
#define SYM_IDENT 289
#define SYM_INT 290
#define SYM_FLOAT 291
#define SYM_STRING 292
#define SYM_PAIRSET 293
#define SYM_AND 294
#define SYM_ASSIGN 295
#define SYM_DOLLAR 296
#define SYM_DONT_MATCH 297
#define SYM_EQUAL 298
#define SYM_GREATER 299
#define SYM_GREATER_EQUAL 300
#define SYM_LESS 301
#define SYM_LESS_EQUAL 302
#define SYM_MATCH 303
#define SYM_MINUS 304
#define SYM_MINUS_ASSIGN 305
#define SYM_MINUS_MINUS 306
#define SYM_NEGATE 307
#define SYM_NOT 308
#define SYM_NOT_EQUAL 309
#define SYM_OR 310
#define SYM_PERCENT 311
#define SYM_PERCENT_ASSIGN 312
#define SYM_PLUS 313
#define SYM_PLUS_ASSIGN 314
#define SYM_PLUS_PLUS 315
#define SYM_STAR 316
#define SYM_STAR_ASSIGN 317
#define SYM_SLASH 318
#define SYM_SLASH_ASSIGN 319
#define SYM_LPAREN 320
#define SYM_RPAREN 321
#define SYM_LBRACK 322
#define SYM_RBRACK 323
#define SYM_LCURLY 324
#define SYM_RCURLY 325
#define SYM_COLON 326
#define SYM_COMMA 327
#define SYM_SEMICOLON 328
#define SYM_CALL 329
#define SYM_LIST 330
#define SYM_KW_STREF 331
#define SYM_IX_STREF 332
#define SYM_ERROR 333

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED

union YYSTYPE
{
#line 21 "rmgrm.y" /* yacc.c:355  */

	int	ival;
	NODE_T	*npval;

#line 287 "y.tab.c" /* yacc.c:355  */
};

typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */

/* Copy the second part of user declarations.  */

#line 304 "y.tab.c" /* yacc.c:358  */

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif

#ifndef YY_ATTRIBUTE
# if (defined __GNUC__                                               \
      && (2 < __GNUC__ || (__GNUC__ == 2 && 96 <= __GNUC_MINOR__)))  \
     || defined __SUNPRO_C && 0x5110 <= __SUNPRO_C
#  define YY_ATTRIBUTE(Spec) __attribute__(Spec)
# else
#  define YY_ATTRIBUTE(Spec) /* empty */
# endif
#endif

#ifndef YY_ATTRIBUTE_PURE
# define YY_ATTRIBUTE_PURE   YY_ATTRIBUTE ((__pure__))
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# define YY_ATTRIBUTE_UNUSED YY_ATTRIBUTE ((__unused__))
#endif

#if !defined _Noreturn \
     && (!defined __STDC_VERSION__ || __STDC_VERSION__ < 201112)
# if defined _MSC_VER && 1200 <= _MSC_VER
#  define _Noreturn __declspec (noreturn)
# else
#  define _Noreturn YY_ATTRIBUTE ((__noreturn__))
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(E) ((void) (E))
#else
# define YYUSE(E) /* empty */
#endif

#if defined __GNUC__ && 407 <= __GNUC__ * 100 + __GNUC_MINOR__
/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN \
    _Pragma ("GCC diagnostic push") \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")\
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# define YY_IGNORE_MAYBE_UNINITIALIZED_END \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif


#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYSIZE_T yynewbytes;                                            \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / sizeof (*yyptr);                          \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, (Count) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYSIZE_T yyi;                         \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  6
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   382

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  79
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  83
/* YYNRULES -- Number of rules.  */
#define YYNRULES  171
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  247

/* YYTRANSLATE[YYX] -- Symbol number corresponding to YYX as returned
   by yylex, with out-of-bounds checking.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   333

#define YYTRANSLATE(YYX)                                                \
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, without out-of-bounds checking.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    60,    61,    62,    63,    64,
      65,    66,    67,    68,    69,    70,    71,    72,    73,    74,
      75,    76,    77,    78
};

#if YYDEBUG
  /* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,   183,   183,   186,   186,   188,   190,   191,   193,   193,
     197,   197,   200,   202,   202,   205,   208,   209,   211,   214,
     215,   216,   221,   223,   231,   232,   233,   234,   235,   236,
     237,   238,   239,   240,   241,   242,   243,   244,   247,   248,
     250,   257,   265,   266,   268,   268,   270,   272,   273,   274,
     276,   279,   280,   282,   283,   284,   285,   286,   287,   288,
     289,   290,   291,   292,   293,   294,   295,   297,   300,   306,
     312,   315,   320,   323,   326,   328,   330,   333,   335,   334,
     339,   342,   346,   345,   350,   351,   354,   353,   358,   361,
     363,   361,   367,   368,   369,   371,   372,   373,   375,   376,
     377,   380,   388,   397,   398,   400,   402,   404,   406,   409,
     410,   413,   414,   417,   418,   419,   422,   424,   425,   426,
     428,   429,   431,   432,   434,   435,   438,   439,   441,   442,
     445,   446,   447,   449,   450,   452,   454,   458,   461,   466,
     469,   474,   475,   476,   477,   480,   483,   484,   486,   495,
     498,   499,   501,   502,   504,   505,   506,   508,   509,   511,
     514,   516,   518,   519,   522,   525,   530,   530,   534,   535,
     538,   541
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || 0
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "SYM_PARMS", "SYM_DESCR", "SYM_SITES",
  "SYM_SCORE", "SYM_SE", "SYM_CTX", "SYM_SS", "SYM_H5", "SYM_H3", "SYM_P5",
  "SYM_P3", "SYM_T1", "SYM_T2", "SYM_T3", "SYM_Q1", "SYM_Q2", "SYM_Q3",
  "SYM_Q4", "SYM_ACCEPT", "SYM_BEGIN", "SYM_BREAK", "SYM_CONTINUE",
  "SYM_ELSE", "SYM_END", "SYM_FOR", "SYM_HOLD", "SYM_IF", "SYM_IN",
  "SYM_REJECT", "SYM_RELEASE", "SYM_WHILE", "SYM_IDENT", "SYM_INT",
  "SYM_FLOAT", "SYM_STRING", "SYM_PAIRSET", "SYM_AND", "SYM_ASSIGN",
  "SYM_DOLLAR", "SYM_DONT_MATCH", "SYM_EQUAL", "SYM_GREATER",
  "SYM_GREATER_EQUAL", "SYM_LESS", "SYM_LESS_EQUAL", "SYM_MATCH",
  "SYM_MINUS", "SYM_MINUS_ASSIGN", "SYM_MINUS_MINUS", "SYM_NEGATE",
  "SYM_NOT", "SYM_NOT_EQUAL", "SYM_OR", "SYM_PERCENT",
  "SYM_PERCENT_ASSIGN", "SYM_PLUS", "SYM_PLUS_ASSIGN", "SYM_PLUS_PLUS",
  "SYM_STAR", "SYM_STAR_ASSIGN", "SYM_SLASH", "SYM_SLASH_ASSIGN",
  "SYM_LPAREN", "SYM_RPAREN", "SYM_LBRACK", "SYM_RBRACK", "SYM_LCURLY",
  "SYM_RCURLY", "SYM_COLON", "SYM_COMMA", "SYM_SEMICOLON", "SYM_CALL",
  "SYM_LIST", "SYM_KW_STREF", "SYM_IX_STREF", "SYM_ERROR", "$accept",
  "program", "parm_part", "$@1", "parm_hdr", "descr_part", "$@2",
  "site_part", "$@3", "score_part", "$@4", "pd_list", "pdef", "se_list",
  "strel", "strhdr", "strtype", "kw_site_list", "kw_site", "site",
  "rule_list", "rule", "$@5", "pattern", "action", "stmt_list", "stmt",
  "accept_stmt", "asgn_stmt", "auto_stmt", "break_stmt", "call_stmt",
  "cmpd_stmt", "continue_stmt", "empty_stmt", "for_stmt", "hold_stmt",
  "if_stmt", "$@6", "reject_stmt", "release_stmt", "while_stmt", "@7",
  "loop_level", "if_hdr", "$@8", "for_hdr", "for_ctrl", "$@9", "$@10",
  "for_init", "for_test", "for_incr", "asgn", "asgn_op", "expr", "conj",
  "compare", "comp_op", "a_expr", "add_op", "term", "mul_op", "factor",
  "pairing", "kw_pairing", "primary", "fcall", "stref", "kw_stref",
  "ix_stref", "lval", "auto_lval", "literal", "ident", "incr_op", "e_list",
  "a_list", "pairset", "$@11", "s_list", "string", "empty", YY_NULLPTR
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[NUM] -- (External) token number corresponding to the
   (internal) symbol number NUM (which must be that of a token).  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   299,   300,   301,   302,   303,   304,
     305,   306,   307,   308,   309,   310,   311,   312,   313,   314,
     315,   316,   317,   318,   319,   320,   321,   322,   323,   324,
     325,   326,   327,   328,   329,   330,   331,   332,   333
};
# endif

#define YYPACT_NINF -145

#define yypact_value_is_default(Yystate) \
  (!!((Yystate) == (-145)))

#define YYTABLE_NINF -172

#define yytable_value_is_error(Yytable_value) \
  0

  /* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
     STATE-NUM.  */
static const yytype_int16 yypact[] =
{
      30,  -145,    40,    54,  -145,    62,  -145,  -145,    65,   -13,
     362,  -145,    38,  -145,  -145,  -145,  -145,   -13,    -6,    39,
    -145,   -25,    44,  -145,  -145,  -145,  -145,  -145,  -145,  -145,
    -145,  -145,  -145,  -145,  -145,  -145,  -145,  -145,   362,    15,
    -145,  -145,   362,  -145,  -145,  -145,  -145,  -145,  -145,  -145,
    -145,  -145,  -145,   299,  -145,  -145,  -145,   -13,    15,   362,
    -145,    52,    13,   236,  -145,  -145,  -145,  -145,   140,   140,
     299,  -145,   -40,  -145,  -145,    37,  -145,    46,   171,    25,
    -145,    63,  -145,  -145,   -14,  -145,  -145,    39,  -145,   -29,
    -145,  -145,    22,    29,  -145,    35,   362,  -145,  -145,    84,
    -145,   236,  -145,  -145,    37,  -145,  -145,  -145,   -32,    69,
     299,   299,   299,  -145,  -145,  -145,  -145,  -145,  -145,  -145,
    -145,  -145,  -145,   299,   299,  -145,  -145,  -145,   299,    35,
     362,   299,   -13,  -145,  -145,  -145,    36,    75,    75,    55,
      44,    56,    49,    44,    58,   138,    59,    84,  -145,  -145,
    -145,  -145,  -145,  -145,  -145,  -145,  -145,  -145,  -145,  -145,
    -145,  -145,   138,   138,    53,    57,    61,    68,  -145,    73,
    -145,    77,    60,   -35,    70,  -145,  -145,   -17,  -145,    25,
    -145,  -145,  -145,    79,    86,  -145,  -145,  -145,    83,    85,
     -13,    87,   299,  -145,    90,   299,    94,  -145,  -145,   103,
    -145,  -145,  -145,  -145,  -145,   138,  -145,  -145,    69,   299,
    -145,  -145,  -145,  -145,   102,  -145,  -145,   100,  -145,  -145,
      37,  -145,    37,  -145,  -145,  -145,  -145,  -145,   105,   113,
     114,   138,   299,  -145,   138,  -145,  -145,  -145,    37,  -145,
    -145,   111,   -13,  -145,  -145,   121,  -145
};

  /* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
     Performed when YYTABLE does not specify something else to do.  Zero
     means the default is an error.  */
static const yytype_uint8 yydefact[] =
{
     171,     6,     0,     0,     3,     7,     1,     8,    12,     0,
       0,    10,    15,   159,   160,   161,     4,    16,     0,     0,
     151,   150,     0,    24,    25,    26,    27,    28,    29,    30,
      31,    32,    33,    34,    35,    36,    37,     9,    19,    21,
      23,    22,     0,    13,     2,    17,    18,   103,   104,   106,
     105,   108,   107,     0,   153,   152,    20,     0,     0,    11,
      38,     0,   139,     0,   154,   155,   170,   156,     0,     0,
       0,   166,     0,   113,   101,   102,   109,   111,   114,   124,
     128,     0,   133,   143,   136,   146,   147,   141,   142,   150,
     158,   157,   164,     0,    39,     0,     0,    47,    48,   166,
      14,    42,    44,    46,    49,   141,   134,   135,     0,     0,
       0,     0,     0,   116,   117,   118,   119,   120,   121,   122,
     127,   123,   126,     0,     0,   130,   132,   131,     0,     0,
       0,     0,     0,   148,    40,   140,     0,    85,    85,     0,
       0,     0,     0,     0,     0,   171,     0,    51,    53,    54,
      55,    56,    57,    58,    59,    60,    61,    62,    63,    64,
      65,    66,   171,   171,     0,     0,   151,     0,    43,     0,
     144,     0,   168,   162,     0,   110,   112,   115,   136,   125,
     129,    41,   138,   137,     0,   165,    67,    84,     0,     0,
     171,     0,     0,    80,     0,     0,     0,    50,    52,    77,
      75,    68,    71,    69,    74,   171,    45,   167,     0,     0,
     149,   145,    70,    73,     0,    89,    92,   151,    94,    76,
      86,    81,    82,    72,    78,   169,   163,    88,     0,     0,
       0,   171,   171,    87,   171,    79,    90,    95,    96,    97,
      83,     0,   171,    91,    98,   151,   100
};

  /* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -145,  -145,  -145,  -145,  -145,  -145,  -145,  -145,  -145,  -145,
    -145,   175,  -145,    93,  -145,     1,  -145,  -145,   129,  -145,
      92,  -145,  -145,  -145,    26,   -94,  -144,  -145,  -145,  -145,
    -145,  -145,  -145,  -145,  -145,  -145,  -145,  -145,  -145,  -145,
    -145,  -145,  -145,    64,  -145,  -145,  -145,  -145,  -145,  -145,
    -145,  -145,  -145,    -5,  -145,   -46,   -82,  -145,  -145,    71,
    -145,    72,  -145,    76,    78,   107,    -4,   -86,   -55,     4,
    -145,    -8,   -91,  -145,    -7,   -15,  -126,    67,   -67,  -145,
      -2,  -106,     0
};

  /* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     2,     3,     9,     4,     8,    10,    12,    42,    44,
      63,    16,    17,    37,    38,    72,    40,    59,    60,    73,
     100,   101,   169,   102,   103,   146,   147,   148,   149,   150,
     151,   152,   153,   154,   155,   156,   157,   158,   231,   159,
     160,   161,   230,   188,   162,   229,   163,   214,   228,   241,
     215,   236,   243,   164,    53,   173,    76,    77,   123,    78,
     124,    79,   128,    80,    81,    61,    82,    83,    84,    85,
      86,   105,    20,    88,    89,    22,   174,    93,    90,   109,
     171,    91,   167
};

  /* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
     positive, shift that token.  If negative, reduce the rule whose
     number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
       5,    19,    21,   172,    18,   184,    54,    75,   166,    19,
      21,    39,    18,   165,    41,    55,  -137,   104,   199,   200,
     111,    13,    14,   111,   108,    57,    14,   110,   134,   175,
     176,    15,   120,     1,   170,    15,   131,   209,    14,    39,
       6,   122,    41,    58,    43,    87,    62,    15,    74,    19,
      21,   196,    92,   198,   166,   104,   166,   130,     7,   165,
      58,   165,   181,    62,   106,   107,    -5,    46,   178,   178,
      11,   166,   166,   178,    54,   183,   165,   165,    13,    47,
      57,   125,    95,   226,    96,   112,   126,   235,   127,    48,
     240,    19,   111,   129,   132,   133,    49,    58,    50,   217,
      62,    51,   172,    52,    71,   136,    66,   137,   138,   186,
     187,   139,   140,   141,   166,   142,   143,   144,    13,   165,
     190,   192,   193,   195,    19,    21,   201,    92,   224,   197,
     202,    56,   208,   191,   203,    14,   194,    19,   210,    19,
     166,   204,   205,   166,    15,   165,   220,   207,   165,   222,
     130,   245,   211,   145,    19,    19,   212,  -171,   213,   136,
     219,   137,   138,   221,   223,   139,   140,   141,   227,   142,
     143,   144,    13,   -93,    13,    64,    65,    66,   232,   233,
     234,    67,    19,    21,   242,   216,   238,   -99,    94,    14,
     218,    14,    45,   168,   177,   206,   179,    19,    15,   185,
      15,     0,   189,   135,   180,    70,   225,   145,   182,    71,
       0,     0,     0,   113,   114,   115,   116,   117,   118,   119,
     120,     0,     0,    19,    87,   121,    19,   237,     0,   122,
       0,     0,   239,     0,    19,    21,     0,   244,     0,     0,
       0,     0,   246,    23,    24,    25,    26,    27,    28,    29,
      30,    31,    32,    33,    34,    35,    36,     0,    97,     0,
       0,     0,    98,     0,     0,     0,     0,     0,     0,     0,
      13,    64,    65,    66,     0,     0,     0,    67,     0,     0,
       0,     0,     0,     0,     0,    68,     0,    14,     0,    69,
       0,     0,     0,     0,     0,     0,    15,     0,     0,     0,
       0,    70,     0,     0,     0,    99,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    13,    64,    65,    66,     0,     0,     0,
      67,     0,     0,     0,     0,     0,     0,     0,    68,     0,
      14,     0,    69,     0,     0,     0,     0,     0,     0,    15,
       0,     0,     0,     0,    70,     0,     0,     0,    71,    23,
      24,    25,    26,    27,    28,    29,    30,    31,    32,    33,
      34,    35,    36
};

static const yytype_int16 yycheck[] =
{
       0,     9,     9,   109,     9,   131,    21,    53,    99,    17,
      17,    10,    17,    99,    10,    22,    30,    63,   162,   163,
      55,    34,    51,    55,    70,    65,    51,    67,    95,   111,
     112,    60,    49,     3,    66,    60,    65,    72,    51,    38,
       0,    58,    38,    42,     6,    53,    42,    60,    53,    57,
      57,   145,    57,   147,   145,   101,   147,    71,     4,   145,
      59,   147,   129,    59,    68,    69,     4,    73,   123,   124,
       5,   162,   163,   128,    89,   130,   162,   163,    34,    40,
      65,    56,    30,   209,    71,    39,    61,   231,    63,    50,
     234,    99,    55,    30,    72,    66,    57,    96,    59,   190,
      96,    62,   208,    64,    69,    21,    37,    23,    24,    73,
      35,    27,    28,    29,   205,    31,    32,    33,    34,   205,
      65,    65,    73,    65,   132,   132,    73,   132,    25,    70,
      73,    38,    72,   140,    73,    51,   143,   145,    68,   147,
     231,    73,    69,   234,    60,   231,   192,    70,   234,   195,
      71,   242,    66,    69,   162,   163,    73,    73,    73,    21,
      73,    23,    24,    73,    70,    27,    28,    29,    66,    31,
      32,    33,    34,    73,    34,    35,    36,    37,    73,    66,
      66,    41,   190,   190,    73,   190,   232,    66,    59,    51,
     190,    51,    17,   101,   123,   169,   124,   205,    60,   132,
      60,    -1,   138,    96,   128,    65,   208,    69,   130,    69,
      -1,    -1,    -1,    42,    43,    44,    45,    46,    47,    48,
      49,    -1,    -1,   231,   232,    54,   234,   232,    -1,    58,
      -1,    -1,   232,    -1,   242,   242,    -1,   242,    -1,    -1,
      -1,    -1,   242,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,    17,    18,    19,    20,    -1,    22,    -1,
      -1,    -1,    26,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      34,    35,    36,    37,    -1,    -1,    -1,    41,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    49,    -1,    51,    -1,    53,
      -1,    -1,    -1,    -1,    -1,    -1,    60,    -1,    -1,    -1,
      -1,    65,    -1,    -1,    -1,    69,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    16,    17,    18,    19,    20,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    34,    35,    36,    37,    -1,    -1,    -1,
      41,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    49,    -1,
      51,    -1,    53,    -1,    -1,    -1,    -1,    -1,    -1,    60,
      -1,    -1,    -1,    -1,    65,    -1,    -1,    -1,    69,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,    17,
      18,    19,    20
};

  /* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
     symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     3,    80,    81,    83,   161,     0,     4,    84,    82,
      85,     5,    86,    34,    51,    60,    90,    91,   132,   150,
     151,   153,   154,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,    17,    18,    19,    20,    92,    93,    94,
      95,   148,    87,     6,    88,    90,    73,    40,    50,    57,
      59,    62,    64,   133,   154,   153,    92,    65,    94,    96,
      97,   144,   148,    89,    35,    36,    37,    41,    49,    53,
      65,    69,    94,    98,   132,   134,   135,   136,   138,   140,
     142,   143,   145,   146,   147,   148,   149,   150,   152,   153,
     157,   160,   132,   156,    97,    30,    71,    22,    26,    69,
      99,   100,   102,   103,   134,   150,   145,   145,   134,   158,
      67,    55,    39,    42,    43,    44,    45,    46,    47,    48,
      49,    54,    58,   137,   139,    56,    61,    63,   141,    30,
      71,    65,    72,    66,   157,   144,    21,    23,    24,    27,
      28,    29,    31,    32,    33,    69,   104,   105,   106,   107,
     108,   109,   110,   111,   112,   113,   114,   115,   116,   118,
     119,   120,   123,   125,   132,   146,   151,   161,    99,   101,
      66,   159,   160,   134,   155,   135,   135,   138,   147,   140,
     142,   157,   143,   147,   155,   156,    73,    35,   122,   122,
      65,   153,    65,    73,   153,    65,   104,    70,   104,   105,
     105,    73,    73,    73,    73,    69,   103,    70,    72,    72,
      68,    66,    73,    73,   126,   129,   132,   151,   161,    73,
     134,    73,   134,    70,    25,   159,   155,    66,   127,   124,
     121,   117,    73,    66,    66,   105,   130,   132,   134,   161,
     105,   128,    73,   131,   132,   151,   161
};

  /* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,    79,    80,    82,    81,    81,    83,    83,    85,    84,
      87,    86,    86,    89,    88,    88,    90,    90,    91,    92,
      92,    93,    93,    94,    95,    95,    95,    95,    95,    95,
      95,    95,    95,    95,    95,    95,    95,    95,    96,    96,
      97,    98,    99,    99,   101,   100,   100,   102,   102,   102,
     103,   104,   104,   105,   105,   105,   105,   105,   105,   105,
     105,   105,   105,   105,   105,   105,   105,   106,   107,   108,
     109,   110,   111,   112,   113,   114,   115,   116,   117,   116,
     118,   119,   121,   120,   122,   122,   124,   123,   125,   127,
     128,   126,   129,   129,   129,   130,   130,   130,   131,   131,
     131,   132,   132,   133,   133,   133,   133,   133,   133,   134,
     134,   135,   135,   136,   136,   136,   137,   137,   137,   137,
     137,   137,   137,   137,   138,   138,   139,   139,   140,   140,
     141,   141,   141,   142,   142,   142,   142,   143,   143,   144,
     144,   145,   145,   145,   145,   146,   147,   147,   148,   149,
     150,   150,   151,   151,   152,   152,   152,   152,   152,   153,
     154,   154,   155,   155,   156,   156,   158,   157,   159,   159,
     160,   161
};

  /* YYR2[YYN] -- Number of symbols on the right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     4,     0,     3,     1,     1,     1,     0,     3,
       0,     3,     0,     0,     3,     0,     1,     2,     2,     1,
       2,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     2,
       3,     3,     1,     2,     0,     3,     1,     1,     1,     1,
       3,     1,     2,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     2,     2,     2,
       3,     2,     3,     3,     2,     2,     3,     2,     0,     5,
       2,     3,     0,     6,     1,     0,     0,     5,     4,     0,
       0,     7,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     3,     3,     1,     1,     1,     1,     1,     1,     1,
       3,     1,     3,     1,     1,     3,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     3,     1,     1,     1,     3,
       1,     1,     1,     1,     2,     2,     1,     1,     3,     1,
       3,     1,     1,     1,     3,     4,     1,     1,     4,     4,
       1,     1,     2,     2,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     3,     1,     3,     0,     4,     1,     3,
       1,     0
};


#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)
#define YYEMPTY         (-2)
#define YYEOF           0

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                  \
do                                                              \
  if (yychar == YYEMPTY)                                        \
    {                                                           \
      yychar = (Token);                                         \
      yylval = (Value);                                         \
      YYPOPSTACK (yylen);                                       \
      yystate = *yyssp;                                         \
      goto yybackup;                                            \
    }                                                           \
  else                                                          \
    {                                                           \
      yyerror (YY_("syntax error: cannot back up")); \
      YYERROR;                                                  \
    }                                                           \
while (0)

/* Error token number */
#define YYTERROR        1
#define YYERRCODE       256



/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)

/* This macro is provided for backward compatibility. */
#ifndef YY_LOCATION_PRINT
# define YY_LOCATION_PRINT(File, Loc) ((void) 0)
#endif


# define YY_SYMBOL_PRINT(Title, Type, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Type, Value); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*----------------------------------------.
| Print this symbol's value on YYOUTPUT.  |
`----------------------------------------*/

static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  FILE *yyo = yyoutput;
  YYUSE (yyo);
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# endif
  YYUSE (yytype);
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  YYFPRINTF (yyoutput, "%s %s (",
             yytype < YYNTOKENS ? "token" : "nterm", yytname[yytype]);

  yy_symbol_value_print (yyoutput, yytype, yyvaluep);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yytype_int16 *yybottom, yytype_int16 *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yytype_int16 *yyssp, YYSTYPE *yyvsp, int yyrule)
{
  unsigned long int yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       yystos[yyssp[yyi + 1 - yynrhs]],
                       &(yyvsp[(yyi + 1) - (yynrhs)])
                                              );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif


#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
static YYSIZE_T
yystrlen (const char *yystr)
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
static char *
yystpcpy (char *yydest, const char *yysrc)
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
        switch (*++yyp)
          {
          case '\'':
          case ',':
            goto do_not_strip_quotes;

          case '\\':
            if (*++yyp != '\\')
              goto do_not_strip_quotes;
            /* Fall through.  */
          default:
            if (yyres)
              yyres[yyn] = *yyp;
            yyn++;
            break;

          case '"':
            if (yyres)
              yyres[yyn] = '\0';
            return yyn;
          }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into *YYMSG, which is of size *YYMSG_ALLOC, an error message
   about the unexpected token YYTOKEN for the state stack whose top is
   YYSSP.

   Return 0 if *YYMSG was successfully written.  Return 1 if *YYMSG is
   not large enough to hold the message.  In that case, also set
   *YYMSG_ALLOC to the required number of bytes.  Return 2 if the
   required number of bytes is too large to store.  */
static int
yysyntax_error (YYSIZE_T *yymsg_alloc, char **yymsg,
                yytype_int16 *yyssp, int yytoken)
{
  YYSIZE_T yysize0 = yytnamerr (YY_NULLPTR, yytname[yytoken]);
  YYSIZE_T yysize = yysize0;
  enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
  /* Internationalized format string. */
  const char *yyformat = YY_NULLPTR;
  /* Arguments of yyformat. */
  char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
  /* Number of reported tokens (one for the "unexpected", one per
     "expected"). */
  int yycount = 0;

  /* There are many possibilities here to consider:
     - If this state is a consistent state with a default action, then
       the only way this function was invoked is if the default action
       is an error action.  In that case, don't check for expected
       tokens because there are none.
     - The only way there can be no lookahead present (in yychar) is if
       this state is a consistent state with a default action.  Thus,
       detecting the absence of a lookahead is sufficient to determine
       that there is no unexpected or expected token to report.  In that
       case, just report a simple "syntax error".
     - Don't assume there isn't a lookahead just because this state is a
       consistent state with a default action.  There might have been a
       previous inconsistent state, consistent state with a non-default
       action, or user semantic action that manipulated yychar.
     - Of course, the expected token list depends on states to have
       correct lookahead information, and it depends on the parser not
       to perform extra reductions after fetching a lookahead from the
       scanner and before detecting a syntax error.  Thus, state merging
       (from LALR or IELR) and default reductions corrupt the expected
       token list.  However, the list is correct for canonical LR with
       one exception: it will still contain any token that will not be
       accepted due to an error action in a later state.
  */
  if (yytoken != YYEMPTY)
    {
      int yyn = yypact[*yyssp];
      yyarg[yycount++] = yytname[yytoken];
      if (!yypact_value_is_default (yyn))
        {
          /* Start YYX at -YYN if negative to avoid negative indexes in
             YYCHECK.  In other words, skip the first -YYN actions for
             this state because they are default actions.  */
          int yyxbegin = yyn < 0 ? -yyn : 0;
          /* Stay within bounds of both yycheck and yytname.  */
          int yychecklim = YYLAST - yyn + 1;
          int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
          int yyx;

          for (yyx = yyxbegin; yyx < yyxend; ++yyx)
            if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR
                && !yytable_value_is_error (yytable[yyx + yyn]))
              {
                if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
                  {
                    yycount = 1;
                    yysize = yysize0;
                    break;
                  }
                yyarg[yycount++] = yytname[yyx];
                {
                  YYSIZE_T yysize1 = yysize + yytnamerr (YY_NULLPTR, yytname[yyx]);
                  if (! (yysize <= yysize1
                         && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
                    return 2;
                  yysize = yysize1;
                }
              }
        }
    }

  switch (yycount)
    {
# define YYCASE_(N, S)                      \
      case N:                               \
        yyformat = S;                       \
      break
      YYCASE_(0, YY_("syntax error"));
      YYCASE_(1, YY_("syntax error, unexpected %s"));
      YYCASE_(2, YY_("syntax error, unexpected %s, expecting %s"));
      YYCASE_(3, YY_("syntax error, unexpected %s, expecting %s or %s"));
      YYCASE_(4, YY_("syntax error, unexpected %s, expecting %s or %s or %s"));
      YYCASE_(5, YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s"));
# undef YYCASE_
    }

  {
    YYSIZE_T yysize1 = yysize + yystrlen (yyformat);
    if (! (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
      return 2;
    yysize = yysize1;
  }

  if (*yymsg_alloc < yysize)
    {
      *yymsg_alloc = 2 * yysize;
      if (! (yysize <= *yymsg_alloc
             && *yymsg_alloc <= YYSTACK_ALLOC_MAXIMUM))
        *yymsg_alloc = YYSTACK_ALLOC_MAXIMUM;
      return 1;
    }

  /* Avoid sprintf, as that infringes on the user's name space.
     Don't have undefined behavior even if the translation
     produced a string with the wrong number of "%s"s.  */
  {
    char *yyp = *yymsg;
    int yyi = 0;
    while ((*yyp = *yyformat) != '\0')
      if (*yyp == '%' && yyformat[1] == 's' && yyi < yycount)
        {
          yyp += yytnamerr (yyp, yyarg[yyi++]);
          yyformat += 2;
        }
      else
        {
          yyp++;
          yyformat++;
        }
  }
  return 0;
}
#endif /* YYERROR_VERBOSE */

/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
{
  YYUSE (yyvaluep);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YYUSE (yytype);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}




/* The lookahead symbol.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;
/* Number of syntax errors so far.  */
int yynerrs;


/*----------.
| yyparse.  |
`----------*/

int
yyparse (void)
{
    int yystate;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus;

    /* The stacks and their tools:
       'yyss': related to states.
       'yyvs': related to semantic values.

       Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    yytype_int16 yyssa[YYINITDEPTH];
    yytype_int16 *yyss;
    yytype_int16 *yyssp;

    /* The semantic value stack.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs;
    YYSTYPE *yyvsp;

    YYSIZE_T yystacksize;

  int yyn;
  int yyresult;
  /* Lookahead token as an internal (translated) token number.  */
  int yytoken = 0;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  yyssp = yyss = yyssa;
  yyvsp = yyvs = yyvsa;
  yystacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY; /* Cause a token to be read.  */
  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        YYSTYPE *yyvs1 = yyvs;
        yytype_int16 *yyss1 = yyss;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * sizeof (*yyssp),
                    &yyvs1, yysize * sizeof (*yyvsp),
                    &yystacksize);

        yyss = yyss1;
        yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yytype_int16 *yyss1 = yyss;
        union yyalloc *yyptr =
          (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
        if (! yyptr)
          goto yyexhaustedlab;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
#  undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
                  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = yylex ();
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token.  */
  yychar = YYEMPTY;

  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
        case 3:
#line 186 "rmgrm.y" /* yacc.c:1646  */
    { rm_context = CTX_PARMS; }
#line 1626 "y.tab.c" /* yacc.c:1646  */
    break;

  case 6:
#line 190 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = NULL; }
#line 1632 "y.tab.c" /* yacc.c:1646  */
    break;

  case 7:
#line 191 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = NULL; }
#line 1638 "y.tab.c" /* yacc.c:1646  */
    break;

  case 8:
#line 193 "rmgrm.y" /* yacc.c:1646  */
    { rm_context = CTX_DESCR; }
#line 1644 "y.tab.c" /* yacc.c:1646  */
    break;

  case 9:
#line 195 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = NULL; }
#line 1650 "y.tab.c" /* yacc.c:1646  */
    break;

  case 10:
#line 197 "rmgrm.y" /* yacc.c:1646  */
    { rm_context = CTX_SITES; }
#line 1656 "y.tab.c" /* yacc.c:1646  */
    break;

  case 11:
#line 199 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = NULL; }
#line 1662 "y.tab.c" /* yacc.c:1646  */
    break;

  case 12:
#line 200 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = NULL; }
#line 1668 "y.tab.c" /* yacc.c:1646  */
    break;

  case 13:
#line 202 "rmgrm.y" /* yacc.c:1646  */
    { rm_context = CTX_SCORE; }
#line 1674 "y.tab.c" /* yacc.c:1646  */
    break;

  case 14:
#line 204 "rmgrm.y" /* yacc.c:1646  */
    { RM_accept(); (yyval.npval) = NULL; }
#line 1680 "y.tab.c" /* yacc.c:1646  */
    break;

  case 15:
#line 205 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = NULL; }
#line 1686 "y.tab.c" /* yacc.c:1646  */
    break;

  case 21:
#line 216 "rmgrm.y" /* yacc.c:1646  */
    { if( rm_context == CTX_DESCR )
					SE_close();
				  else if( rm_context == CTX_SITES )
					POS_close();
				}
#line 1696 "y.tab.c" /* yacc.c:1646  */
    break;

  case 23:
#line 223 "rmgrm.y" /* yacc.c:1646  */
    { if( rm_context == CTX_DESCR )
					SE_open( (yyvsp[0].ival) );
				  else if( rm_context == CTX_SITES )
					POS_open( (yyvsp[0].ival) );
				  else
					(yyval.npval) = RM_node( (yyvsp[0].ival), 0, 0, 0 );
				}
#line 1708 "y.tab.c" /* yacc.c:1646  */
    break;

  case 24:
#line 231 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_SE; }
#line 1714 "y.tab.c" /* yacc.c:1646  */
    break;

  case 25:
#line 232 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_CTX; }
#line 1720 "y.tab.c" /* yacc.c:1646  */
    break;

  case 26:
#line 233 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_SS; }
#line 1726 "y.tab.c" /* yacc.c:1646  */
    break;

  case 27:
#line 234 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_H5; }
#line 1732 "y.tab.c" /* yacc.c:1646  */
    break;

  case 28:
#line 235 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_H3; }
#line 1738 "y.tab.c" /* yacc.c:1646  */
    break;

  case 29:
#line 236 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_P5; }
#line 1744 "y.tab.c" /* yacc.c:1646  */
    break;

  case 30:
#line 237 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_P3; }
#line 1750 "y.tab.c" /* yacc.c:1646  */
    break;

  case 31:
#line 238 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_T1; }
#line 1756 "y.tab.c" /* yacc.c:1646  */
    break;

  case 32:
#line 239 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_T2; }
#line 1762 "y.tab.c" /* yacc.c:1646  */
    break;

  case 33:
#line 240 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_T3; }
#line 1768 "y.tab.c" /* yacc.c:1646  */
    break;

  case 34:
#line 241 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_Q1; }
#line 1774 "y.tab.c" /* yacc.c:1646  */
    break;

  case 35:
#line 242 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_Q2; }
#line 1780 "y.tab.c" /* yacc.c:1646  */
    break;

  case 36:
#line 243 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_Q3; }
#line 1786 "y.tab.c" /* yacc.c:1646  */
    break;

  case 37:
#line 244 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_Q4; }
#line 1792 "y.tab.c" /* yacc.c:1646  */
    break;

  case 40:
#line 251 "rmgrm.y" /* yacc.c:1646  */
    { if( rm_context == CTX_SITES )
					SI_close( (yyvsp[0].npval) );
				  else if( rm_context == CTX_SCORE )
					(yyval.npval) = RM_node( SYM_IN, 0, (yyvsp[-2].npval), (yyvsp[0].npval) );
				}
#line 1802 "y.tab.c" /* yacc.c:1646  */
    break;

  case 41:
#line 258 "rmgrm.y" /* yacc.c:1646  */
    { if( rm_context == CTX_SITES )
					SI_close( (yyvsp[0].npval) );
				  else if( rm_context == CTX_SCORE )
					(yyval.npval) = RM_node( SYM_IN, 0, (yyvsp[-2].npval), (yyvsp[0].npval) );
				}
#line 1812 "y.tab.c" /* yacc.c:1646  */
    break;

  case 44:
#line 268 "rmgrm.y" /* yacc.c:1646  */
    { RM_action( (yyvsp[0].npval) ); }
#line 1818 "y.tab.c" /* yacc.c:1646  */
    break;

  case 45:
#line 269 "rmgrm.y" /* yacc.c:1646  */
    { RM_endaction(); }
#line 1824 "y.tab.c" /* yacc.c:1646  */
    break;

  case 47:
#line 272 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( SYM_BEGIN, 0, 0, 0 ); }
#line 1830 "y.tab.c" /* yacc.c:1646  */
    break;

  case 48:
#line 273 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( SYM_END, 0, 0, 0 ); }
#line 1836 "y.tab.c" /* yacc.c:1646  */
    break;

  case 49:
#line 274 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 1842 "y.tab.c" /* yacc.c:1646  */
    break;

  case 50:
#line 277 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = NULL; }
#line 1848 "y.tab.c" /* yacc.c:1646  */
    break;

  case 67:
#line 298 "rmgrm.y" /* yacc.c:1646  */
    { RM_accept(); (yyval.npval) = NULL; }
#line 1854 "y.tab.c" /* yacc.c:1646  */
    break;

  case 68:
#line 301 "rmgrm.y" /* yacc.c:1646  */
    { RM_mark();
				  RM_expr( 0, (yyvsp[-1].npval) );
				  RM_clear();
				}
#line 1863 "y.tab.c" /* yacc.c:1646  */
    break;

  case 69:
#line 307 "rmgrm.y" /* yacc.c:1646  */
    { RM_mark();
				  RM_expr( 0, (yyvsp[-1].npval) );
				  RM_clear();
				}
#line 1872 "y.tab.c" /* yacc.c:1646  */
    break;

  case 70:
#line 313 "rmgrm.y" /* yacc.c:1646  */
    { RM_break( (yyvsp[-1].npval) ); (yyval.npval) = NULL; }
#line 1878 "y.tab.c" /* yacc.c:1646  */
    break;

  case 71:
#line 316 "rmgrm.y" /* yacc.c:1646  */
    { RM_expr( 0, (yyvsp[-1].npval) );
				  RM_clear();
				}
#line 1886 "y.tab.c" /* yacc.c:1646  */
    break;

  case 72:
#line 321 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = NULL; }
#line 1892 "y.tab.c" /* yacc.c:1646  */
    break;

  case 73:
#line 324 "rmgrm.y" /* yacc.c:1646  */
    { RM_continue( (yyvsp[-1].npval) ); (yyval.npval) = NULL; }
#line 1898 "y.tab.c" /* yacc.c:1646  */
    break;

  case 75:
#line 328 "rmgrm.y" /* yacc.c:1646  */
    { RM_endfor(); }
#line 1904 "y.tab.c" /* yacc.c:1646  */
    break;

  case 76:
#line 331 "rmgrm.y" /* yacc.c:1646  */
    { RM_hold( (yyvsp[-1].npval) ); }
#line 1910 "y.tab.c" /* yacc.c:1646  */
    break;

  case 77:
#line 333 "rmgrm.y" /* yacc.c:1646  */
    { RM_endif(); }
#line 1916 "y.tab.c" /* yacc.c:1646  */
    break;

  case 78:
#line 335 "rmgrm.y" /* yacc.c:1646  */
    { RM_else(); }
#line 1922 "y.tab.c" /* yacc.c:1646  */
    break;

  case 79:
#line 337 "rmgrm.y" /* yacc.c:1646  */
    { RM_endelse(); }
#line 1928 "y.tab.c" /* yacc.c:1646  */
    break;

  case 80:
#line 340 "rmgrm.y" /* yacc.c:1646  */
    { RM_reject(); (yyval.npval) = NULL; }
#line 1934 "y.tab.c" /* yacc.c:1646  */
    break;

  case 81:
#line 343 "rmgrm.y" /* yacc.c:1646  */
    { RM_release( (yyvsp[-1].npval) ); }
#line 1940 "y.tab.c" /* yacc.c:1646  */
    break;

  case 82:
#line 346 "rmgrm.y" /* yacc.c:1646  */
    { RM_while( (yyvsp[0].npval) ); (yyval.npval) = NULL; }
#line 1946 "y.tab.c" /* yacc.c:1646  */
    break;

  case 83:
#line 348 "rmgrm.y" /* yacc.c:1646  */
    { RM_endwhile(); (yyval.npval) = NULL; }
#line 1952 "y.tab.c" /* yacc.c:1646  */
    break;

  case 84:
#line 350 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( SYM_INT, &rm_tokval, 0, 0 ); }
#line 1958 "y.tab.c" /* yacc.c:1646  */
    break;

  case 85:
#line 351 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = NULL; }
#line 1964 "y.tab.c" /* yacc.c:1646  */
    break;

  case 86:
#line 354 "rmgrm.y" /* yacc.c:1646  */
    { RM_if( (yyvsp[0].npval) ); }
#line 1970 "y.tab.c" /* yacc.c:1646  */
    break;

  case 87:
#line 356 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = NULL; }
#line 1976 "y.tab.c" /* yacc.c:1646  */
    break;

  case 88:
#line 359 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = NULL; }
#line 1982 "y.tab.c" /* yacc.c:1646  */
    break;

  case 89:
#line 361 "rmgrm.y" /* yacc.c:1646  */
    {  RM_forinit( (yyvsp[0].npval) ); }
#line 1988 "y.tab.c" /* yacc.c:1646  */
    break;

  case 90:
#line 363 "rmgrm.y" /* yacc.c:1646  */
    { RM_fortest( (yyvsp[0].npval) ); }
#line 1994 "y.tab.c" /* yacc.c:1646  */
    break;

  case 91:
#line 365 "rmgrm.y" /* yacc.c:1646  */
    { RM_forincr( (yyvsp[0].npval) ); }
#line 2000 "y.tab.c" /* yacc.c:1646  */
    break;

  case 92:
#line 367 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2006 "y.tab.c" /* yacc.c:1646  */
    break;

  case 93:
#line 368 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2012 "y.tab.c" /* yacc.c:1646  */
    break;

  case 94:
#line 369 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2018 "y.tab.c" /* yacc.c:1646  */
    break;

  case 95:
#line 371 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2024 "y.tab.c" /* yacc.c:1646  */
    break;

  case 96:
#line 372 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2030 "y.tab.c" /* yacc.c:1646  */
    break;

  case 97:
#line 373 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2036 "y.tab.c" /* yacc.c:1646  */
    break;

  case 98:
#line 375 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2042 "y.tab.c" /* yacc.c:1646  */
    break;

  case 99:
#line 376 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2048 "y.tab.c" /* yacc.c:1646  */
    break;

  case 100:
#line 377 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2054 "y.tab.c" /* yacc.c:1646  */
    break;

  case 101:
#line 381 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( (yyvsp[-1].ival), 0, (yyvsp[-2].npval), (yyvsp[0].npval) );
				  if( rm_context == CTX_PARMS )
					PARM_add( (yyval.npval) );
				  else if( rm_context == CTX_DESCR ||
					rm_context == CTX_SITES )
					SE_addval( (yyval.npval) );
				}
#line 2066 "y.tab.c" /* yacc.c:1646  */
    break;

  case 102:
#line 389 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( (yyvsp[-1].ival), 0, (yyvsp[-2].npval), (yyvsp[0].npval) );
				  if( rm_context == CTX_PARMS )
					PARM_add( (yyval.npval) );
				  else if( rm_context == CTX_DESCR ||
					rm_context == CTX_SITES )
					SE_addval( (yyval.npval) );
				}
#line 2078 "y.tab.c" /* yacc.c:1646  */
    break;

  case 103:
#line 397 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_ASSIGN; }
#line 2084 "y.tab.c" /* yacc.c:1646  */
    break;

  case 104:
#line 399 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_MINUS_ASSIGN; }
#line 2090 "y.tab.c" /* yacc.c:1646  */
    break;

  case 105:
#line 401 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_PLUS_ASSIGN; }
#line 2096 "y.tab.c" /* yacc.c:1646  */
    break;

  case 106:
#line 403 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_PERCENT_ASSIGN; }
#line 2102 "y.tab.c" /* yacc.c:1646  */
    break;

  case 107:
#line 405 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_SLASH_ASSIGN; }
#line 2108 "y.tab.c" /* yacc.c:1646  */
    break;

  case 108:
#line 407 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_STAR_ASSIGN; }
#line 2114 "y.tab.c" /* yacc.c:1646  */
    break;

  case 109:
#line 409 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2120 "y.tab.c" /* yacc.c:1646  */
    break;

  case 110:
#line 411 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( SYM_OR, 0, (yyvsp[-2].npval), (yyvsp[0].npval) ); }
#line 2126 "y.tab.c" /* yacc.c:1646  */
    break;

  case 111:
#line 413 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2132 "y.tab.c" /* yacc.c:1646  */
    break;

  case 112:
#line 415 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( SYM_AND, 0, (yyvsp[-2].npval), (yyvsp[0].npval) ); }
#line 2138 "y.tab.c" /* yacc.c:1646  */
    break;

  case 113:
#line 417 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2144 "y.tab.c" /* yacc.c:1646  */
    break;

  case 114:
#line 418 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2150 "y.tab.c" /* yacc.c:1646  */
    break;

  case 115:
#line 420 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( (yyvsp[-1].ival), 0, (yyvsp[-2].npval), (yyvsp[0].npval) ); }
#line 2156 "y.tab.c" /* yacc.c:1646  */
    break;

  case 116:
#line 423 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_DONT_MATCH; }
#line 2162 "y.tab.c" /* yacc.c:1646  */
    break;

  case 117:
#line 424 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_EQUAL; }
#line 2168 "y.tab.c" /* yacc.c:1646  */
    break;

  case 118:
#line 425 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_GREATER; }
#line 2174 "y.tab.c" /* yacc.c:1646  */
    break;

  case 119:
#line 427 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_GREATER_EQUAL; }
#line 2180 "y.tab.c" /* yacc.c:1646  */
    break;

  case 120:
#line 428 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_LESS; }
#line 2186 "y.tab.c" /* yacc.c:1646  */
    break;

  case 121:
#line 430 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_LESS_EQUAL; }
#line 2192 "y.tab.c" /* yacc.c:1646  */
    break;

  case 122:
#line 431 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_MATCH; }
#line 2198 "y.tab.c" /* yacc.c:1646  */
    break;

  case 123:
#line 432 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_NOT_EQUAL; }
#line 2204 "y.tab.c" /* yacc.c:1646  */
    break;

  case 124:
#line 434 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2210 "y.tab.c" /* yacc.c:1646  */
    break;

  case 125:
#line 436 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( (yyvsp[-1].ival), 0, (yyvsp[-2].npval), (yyvsp[0].npval) ); }
#line 2216 "y.tab.c" /* yacc.c:1646  */
    break;

  case 126:
#line 438 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_PLUS; }
#line 2222 "y.tab.c" /* yacc.c:1646  */
    break;

  case 127:
#line 439 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_MINUS; }
#line 2228 "y.tab.c" /* yacc.c:1646  */
    break;

  case 128:
#line 441 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2234 "y.tab.c" /* yacc.c:1646  */
    break;

  case 129:
#line 443 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( (yyvsp[-1].ival), 0, (yyvsp[-2].npval), (yyvsp[0].npval) ); }
#line 2240 "y.tab.c" /* yacc.c:1646  */
    break;

  case 130:
#line 445 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_PERCENT; }
#line 2246 "y.tab.c" /* yacc.c:1646  */
    break;

  case 131:
#line 446 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_SLASH; }
#line 2252 "y.tab.c" /* yacc.c:1646  */
    break;

  case 132:
#line 447 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_STAR; }
#line 2258 "y.tab.c" /* yacc.c:1646  */
    break;

  case 133:
#line 449 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2264 "y.tab.c" /* yacc.c:1646  */
    break;

  case 134:
#line 451 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( SYM_NEGATE, 0, 0, (yyvsp[0].npval) ); }
#line 2270 "y.tab.c" /* yacc.c:1646  */
    break;

  case 135:
#line 453 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( SYM_NOT, 0, 0, (yyvsp[0].npval) ); }
#line 2276 "y.tab.c" /* yacc.c:1646  */
    break;

  case 136:
#line 454 "rmgrm.y" /* yacc.c:1646  */
    { if( rm_context == CTX_SCORE )
					(yyval.npval) = (yyvsp[0].npval);
				}
#line 2284 "y.tab.c" /* yacc.c:1646  */
    break;

  case 137:
#line 458 "rmgrm.y" /* yacc.c:1646  */
    { if( rm_context == CTX_SCORE )
					(yyval.npval) = (yyvsp[0].npval);
				}
#line 2292 "y.tab.c" /* yacc.c:1646  */
    break;

  case 138:
#line 462 "rmgrm.y" /* yacc.c:1646  */
    { if( rm_context == CTX_SCORE )
					(yyval.npval) = RM_node( SYM_COLON, 0, (yyvsp[-2].npval), (yyvsp[0].npval) );
				}
#line 2300 "y.tab.c" /* yacc.c:1646  */
    break;

  case 139:
#line 466 "rmgrm.y" /* yacc.c:1646  */
    { if( rm_context == CTX_SCORE )
					(yyval.npval) = (yyvsp[0].npval);
				}
#line 2308 "y.tab.c" /* yacc.c:1646  */
    break;

  case 140:
#line 470 "rmgrm.y" /* yacc.c:1646  */
    { if( rm_context == CTX_SCORE )
					(yyval.npval) = RM_node( SYM_COLON, 0, (yyvsp[-2].npval), (yyvsp[0].npval) );
				}
#line 2316 "y.tab.c" /* yacc.c:1646  */
    break;

  case 141:
#line 474 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2322 "y.tab.c" /* yacc.c:1646  */
    break;

  case 142:
#line 475 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2328 "y.tab.c" /* yacc.c:1646  */
    break;

  case 143:
#line 476 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2334 "y.tab.c" /* yacc.c:1646  */
    break;

  case 144:
#line 478 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[-1].npval); }
#line 2340 "y.tab.c" /* yacc.c:1646  */
    break;

  case 145:
#line 481 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( SYM_CALL, 0, (yyvsp[-3].npval), (yyvsp[-1].npval) ); }
#line 2346 "y.tab.c" /* yacc.c:1646  */
    break;

  case 146:
#line 483 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2352 "y.tab.c" /* yacc.c:1646  */
    break;

  case 147:
#line 484 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2358 "y.tab.c" /* yacc.c:1646  */
    break;

  case 148:
#line 487 "rmgrm.y" /* yacc.c:1646  */
    { if( rm_context == CTX_DESCR )
					SE_close();
				  else if( rm_context == CTX_SITES )
					POS_close();
				  else if( rm_context == CTX_SCORE )
					(yyval.npval) = RM_node( SYM_KW_STREF, 0, (yyvsp[-3].npval), (yyvsp[-1].npval) );
				}
#line 2370 "y.tab.c" /* yacc.c:1646  */
    break;

  case 149:
#line 496 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( SYM_IX_STREF, 0, (yyvsp[-3].npval), (yyvsp[-1].npval) ); }
#line 2376 "y.tab.c" /* yacc.c:1646  */
    break;

  case 150:
#line 498 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2382 "y.tab.c" /* yacc.c:1646  */
    break;

  case 151:
#line 499 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2388 "y.tab.c" /* yacc.c:1646  */
    break;

  case 152:
#line 501 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( (yyvsp[-1].ival), 0, 0, (yyvsp[0].npval) ); }
#line 2394 "y.tab.c" /* yacc.c:1646  */
    break;

  case 153:
#line 502 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( (yyvsp[0].ival), 0, (yyvsp[-1].npval), 0 ); }
#line 2400 "y.tab.c" /* yacc.c:1646  */
    break;

  case 154:
#line 504 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( SYM_INT, &rm_tokval, 0, 0 ); }
#line 2406 "y.tab.c" /* yacc.c:1646  */
    break;

  case 155:
#line 505 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( SYM_FLOAT, &rm_tokval, 0, 0 ); }
#line 2412 "y.tab.c" /* yacc.c:1646  */
    break;

  case 156:
#line 506 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( SYM_DOLLAR,
					&rm_tokval, 0, 0 ); }
#line 2419 "y.tab.c" /* yacc.c:1646  */
    break;

  case 157:
#line 508 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2425 "y.tab.c" /* yacc.c:1646  */
    break;

  case 158:
#line 509 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = (yyvsp[0].npval); }
#line 2431 "y.tab.c" /* yacc.c:1646  */
    break;

  case 159:
#line 511 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( SYM_IDENT,
					&rm_tokval, 0, 0 ); }
#line 2438 "y.tab.c" /* yacc.c:1646  */
    break;

  case 160:
#line 515 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_MINUS_MINUS; }
#line 2444 "y.tab.c" /* yacc.c:1646  */
    break;

  case 161:
#line 516 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.ival) = SYM_PLUS_PLUS; }
#line 2450 "y.tab.c" /* yacc.c:1646  */
    break;

  case 162:
#line 518 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( SYM_LIST, 0, (yyvsp[0].npval), 0 ); }
#line 2456 "y.tab.c" /* yacc.c:1646  */
    break;

  case 163:
#line 520 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( SYM_LIST, 0, (yyvsp[-2].npval), (yyvsp[0].npval) ); }
#line 2462 "y.tab.c" /* yacc.c:1646  */
    break;

  case 164:
#line 522 "rmgrm.y" /* yacc.c:1646  */
    { if( rm_context == CTX_SCORE )
					(yyval.npval) = RM_node( SYM_LIST, 0, (yyvsp[0].npval), 0 );
				}
#line 2470 "y.tab.c" /* yacc.c:1646  */
    break;

  case 165:
#line 526 "rmgrm.y" /* yacc.c:1646  */
    { if( rm_context == CTX_SCORE )
					(yyval.npval) = RM_node( SYM_LIST, 0, (yyvsp[-2].npval), (yyvsp[0].npval) );
				}
#line 2478 "y.tab.c" /* yacc.c:1646  */
    break;

  case 166:
#line 530 "rmgrm.y" /* yacc.c:1646  */
    { PR_open(); }
#line 2484 "y.tab.c" /* yacc.c:1646  */
    break;

  case 167:
#line 532 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = PR_close(); }
#line 2490 "y.tab.c" /* yacc.c:1646  */
    break;

  case 168:
#line 534 "rmgrm.y" /* yacc.c:1646  */
    { PR_add( (yyval.npval) ); }
#line 2496 "y.tab.c" /* yacc.c:1646  */
    break;

  case 169:
#line 536 "rmgrm.y" /* yacc.c:1646  */
    { PR_add( (yyvsp[-2].npval) ) ; }
#line 2502 "y.tab.c" /* yacc.c:1646  */
    break;

  case 170:
#line 538 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = RM_node( SYM_STRING,
					&rm_tokval, 0, 0 ); }
#line 2509 "y.tab.c" /* yacc.c:1646  */
    break;

  case 171:
#line 541 "rmgrm.y" /* yacc.c:1646  */
    { (yyval.npval) = NULL; }
#line 2515 "y.tab.c" /* yacc.c:1646  */
    break;


#line 2519 "y.tab.c" /* yacc.c:1646  */
      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYEMPTY : YYTRANSLATE (yychar);

  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
# define YYSYNTAX_ERROR yysyntax_error (&yymsg_alloc, &yymsg, \
                                        yyssp, yytoken)
      {
        char const *yymsgp = YY_("syntax error");
        int yysyntax_error_status;
        yysyntax_error_status = YYSYNTAX_ERROR;
        if (yysyntax_error_status == 0)
          yymsgp = yymsg;
        else if (yysyntax_error_status == 1)
          {
            if (yymsg != yymsgbuf)
              YYSTACK_FREE (yymsg);
            yymsg = (char *) YYSTACK_ALLOC (yymsg_alloc);
            if (!yymsg)
              {
                yymsg = yymsgbuf;
                yymsg_alloc = sizeof yymsgbuf;
                yysyntax_error_status = 2;
              }
            else
              {
                yysyntax_error_status = YYSYNTAX_ERROR;
                yymsgp = yymsg;
              }
          }
        yyerror (yymsgp);
        if (yysyntax_error_status == 2)
          goto yyexhaustedlab;
      }
# undef YYSYNTAX_ERROR
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYTERROR;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;


      yydestruct ("Error: popping",
                  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#if !defined yyoverflow || YYERROR_VERBOSE
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  yystos[*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  return yyresult;
}
#line 543 "rmgrm.y" /* yacc.c:1906  */


#include "lex.yy.c"

int	yyerror( msg )
char	msg[];
{

	fprintf( stderr, "yyerror: %s\n", msg );
	return( 0 );
}
