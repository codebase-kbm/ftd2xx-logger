#include <windows.h>
#include "loader.h"

BOOL WINAPI DllMain(
    HINSTANCE hinstDLL,
    DWORD fdwReason,
    LPVOID lpReserved)
{
    switch (fdwReason)
    {
        case DLL_PROCESS_ATTACH:
            DisableThreadLibraryCalls(hinstDLL);
            LoadOriginalDll();
            break;

        case DLL_PROCESS_DETACH:
            UnloadOriginalDll();
            break;
    }

    return TRUE;
}