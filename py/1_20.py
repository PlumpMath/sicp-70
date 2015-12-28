#! /usr/bin/env python

# 正则序求值: 完全展开而后归约
# 应用序求值: 先求值参数而后应用

# http://community.schemewiki.org/?sicp-ex-1.20
# 正则序求值,在有判断的情况下需要对当前的值进行求值,如果不满足，继续使用正则序求值
