#include "logger.h"

#include <windows.h>
#include <shlobj.h>
#include <filesystem>
#include <fstream>
#include <string>

namespace fs = std::filesystem;

static std::string GetLogPath()
{
    char path[MAX_PATH];

    if (SHGetFolderPathA(
            nullptr,
            CSIDL_DESKTOP,
            nullptr,
            0,
            path) != S_OK)
    {
        return "ftd2xx-proxy.log";
    }

    fs::path logDir = fs::path(path) / "ftd2xx-proxy";

    std::error_code ec;
    fs::create_directories(logDir, ec);

    return (logDir / "ftd2xx-proxy.log").string();
}


void Log(const char* text)
{
    OutputDebugStringA(text);

    static std::string logFile = GetLogPath();

    std::ofstream file(
        logFile,
        std::ios::app
    );

    if (!file.is_open())
    {
        OutputDebugStringA(
            "ftd2xx-proxy: cannot open logfile\n"
        );
        return;
    }

    file << text << "\n";
    file.flush();
}