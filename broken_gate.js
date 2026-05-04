const express = require('express');
const router = express.Router();
const { exec } = require('child_process');

router.get('/status', (req, res) => {
    const cmd = req.query.cmd;

    // 1. Command Injection (exec with unsanitized input)
    // Semgrep Rule: javascript.lang.security.audit.child-process-exec-no-validation
    exec(`ping -c 1 ${cmd}`, (error, stdout, stderr) => {
        res.send(stdout);
    });

    // 2. Sensitive Cookie without Secure/HttpOnly flags
    // Semgrep Rule: javascript.express.security.audit.res-cookie-no-httponly
    res.cookie('sessionID', '123456', { secure: false });

    // 3. Eval() is Evil
    // Semgrep Rule: javascript.lang.security.audit.eval-with-expression
    const result = eval(req.query.calculation); 
});

// 4. Broken Cryptography (Using MD5)
// Semgrep Rule: javascript.lang.security.audit.crypto-md5-usage
const crypto = require('crypto');
const hash = crypto.createHash('md5').update('password123').digest('hex');

module.exports = router;
