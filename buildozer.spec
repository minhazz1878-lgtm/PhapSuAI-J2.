[app]
title = Phap Su AI
package.name = phapsuai
package.domain = org.minh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,gguf
version = 0.1
requirements = python3,kivy
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE
android.archs = armeabi-v7a, arm64-v8a
android.minapi = 21
android.sdk = 31

[buildozer]
log_level = 2
warn_on_root = 1
