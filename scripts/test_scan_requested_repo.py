import json, tempfile, unittest
from pathlib import Path
import importlib.util

spec=importlib.util.spec_from_file_location('scan', Path(__file__).with_name('scan_requested_repo.py'))
scan=importlib.util.module_from_spec(spec)
spec.loader.exec_module(scan)

class ScanRequestTests(unittest.TestCase):
    def event(self, body):
        f=tempfile.NamedTemporaryFile('w+',delete=False)
        json.dump({'issue':{'number':1,'body':body}},f); f.close()
        return f.name

    def test_parses_authorized_canonical_repo(self):
        p=self.event('### Repository URL\n\nhttps://github.com/OpenHands/automation\n\n### Preferred mode\n\nPublic historical scan\n\n### Authorization\n\n- [x] '+scan.AUTH_TEXT)
        req=scan.parse_issue(p)
        self.assertTrue(req['authorized'])
        self.assertEqual(req['repo_url'],'https://github.com/OpenHands/automation')
        self.assertIsNotNone(scan.REPO_RE.match(req['repo_url']))

    def test_missing_checkbox_is_not_authorized(self):
        p=self.event('### Repository URL\n\nhttps://github.com/OpenHands/automation\n\n### Preferred mode\n\nPublic historical scan')
        self.assertFalse(scan.parse_issue(p)['authorized'])

    def test_non_github_url_rejected(self):
        self.assertIsNone(scan.REPO_RE.match('https://example.com/owner/repo'))

    def test_nested_or_query_url_rejected(self):
        self.assertIsNone(scan.REPO_RE.match('https://github.com/owner/repo/issues'))
        self.assertIsNone(scan.REPO_RE.match('https://github.com/owner/repo?x=1'))

if __name__=='__main__': unittest.main()
