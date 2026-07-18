#pragma once
#include <windows.h>
#include <cstdio>
#include <sstream>

void WriteLog(const std::string& text);

void LogEnter(const char* function);
void LogExit(const char* function);

// Templete Function must be in the Header
template<typename T>
void LogExit(const char* function, T result)
{
    std::ostringstream ss;

    ss << "[EXIT] "
       << function
       << " = "
       << result;

    WriteLog(ss.str());
}
