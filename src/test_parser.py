import unittest
from parser import parse_xml_to_config, eval_expression

class TestParser(unittest.TestCase):

    def test_parse_constants(self):
        xml_data = '''
        <config>
            <constants>
                <constant name="PI">3.14</constant>
                <constant name="E">2.71</constant>
            </constants>
        </config>
        '''
        config = parse_xml_to_config(xml_data)
        self.assertEqual(config['PI'], 3.14)
        self.assertEqual(config['E'], 2.71)

    def test_parse_arrays(self):
        xml_data = '''
        <config>
            <arrays>
                <array name="numbers">
                    <value>1</value>
                    <value>2</value>
                    <value>3</value>
                </array>
            </arrays>
        </config>
        '''
        config = parse_xml_to_config(xml_data)
        self.assertEqual(config['numbers'], [1, 2, 3])

    def test_parse_dictionaries(self):
        xml_data = '''
        <config>
            <dictionaries>
                <dict name="server_config">
                    <entry key="server_name">example.com</entry>
                    <entry key="listen_port">80</entry>
                </dict>
            </dictionaries>
        </config>
        '''
        config = parse_xml_to_config(xml_data)
        self.assertEqual(config['server_config']['server_name'], 'example.com')
        self.assertEqual(config['server_config']['listen_port'], 80)

    def test_parse_web_example(self):
        xml_data = '''
        <config>
            <constants>
                <constant name="web_root">/var/www/html</constant>
                <constant name="listen_port">80</constant>
            </constants>
            <arrays>
                <array name="allowed_ips">
                    <value>192.168.1.1</value>
                    <value>192.168.1.2</value>
                </array>
            </arrays>
            <dictionaries>
                <dict name="server_config">
                    <entry key="server_name">example.com</entry>
                    <entry key="document_root">/var/www/html</entry>
                </dict>
            </dictionaries>
        </config>
        '''
        config = parse_xml_to_config(xml_data)
        self.assertEqual(config['web_root'], '/var/www/html')
        self.assertEqual(config['listen_port'], 80)
        self.assertEqual(config['allowed_ips'], ['192.168.1.1', '192.168.1.2'])
        self.assertEqual(config['server_config']['server_name'], 'example.com')

    def test_eval_expression(self):
        self.assertEqual(eval_expression("3 + 5"), 8)
        self.assertEqual(eval_expression("math.sqrt(16)"), 4.0)
        self.assertEqual(eval_expression("len([1, 2, 3])"), 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)
