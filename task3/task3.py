import json
import sys

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def create_value_dict(values):
    return {item['id']: item['value'] for item in values['values']}

def fill_report_structure(tests, value_dict):
    for test in tests:
        if isinstance(test, dict):
            test_id = test.get('id')
            if test_id in value_dict:
                test['value'] = value_dict[test_id]
            else:
                test['value'] = None

            if 'values' in test:
                fill_report_structure(test['values'], value_dict)
        else:
            print("Warning: Expected a dictionary")

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    if len(sys.argv) == 4:
        values_file = sys.argv[1]
        tests_file = sys.argv[2]
        report_file = sys.argv[3]
    
        values = load_json(values_file)
        tests = load_json(tests_file)
        value_dict = create_value_dict(values)

        fill_report_structure(tests['tests'], value_dict)
        save_json(report_file, tests)
    
    else:
        print('Expected 4 arguments')