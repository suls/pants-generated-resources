# pants-generated-resources [![Build Status](https://travis-ci.org/suls/pants-generated-resources.svg?branch=master)](https://travis-ci.org/suls/pants-generated-resources)

this is a proof-of-concept showing how to _generate_ resources that are then available on the classpath.

## what works

the current implementation works for both

* `./pants run `
* `./pants bundle `

## what doesn't

surprisingly it doesn't work with `./pants bundle --bundle-jvm-deployjar` — the generated resource is ignored in the resulting deployjar.

## current status

* trying to find out why resource is lost in deployjar
* looking into synthetic targets as alternative approach
