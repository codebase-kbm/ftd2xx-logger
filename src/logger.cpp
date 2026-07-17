#include "logger.h"

#include <fstream>
#include <mutex>

static std::mutex g_LogMutex;

void Log(const char* text)
{
    std::lock_guard<std::mutex> lock(g_LogMutex);

    std::ofstream file(
        "td2xx-proxy.log",
        std::ios::app
    );

    file << text << "\n";
}