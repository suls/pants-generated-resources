java_library(
  sources=globs('*.java'),
)

jvm_binary(
  name='main',
  basename='jar-tool',
  main='org.suls.pants.Main',
  dependencies=[
    ':pants',
  ],
)