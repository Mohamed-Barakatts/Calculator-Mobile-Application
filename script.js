document.addEventListener('DOMContentLoaded', function() {
    const calculator = {
        screen: document.querySelector('.calculator-screen'),
        keys: document.querySelector('.calculator-keys'),
        screenValue: '',
        lastInput: '',
        operators: ['+', '-', '*', '/', '^', '%', '√']
    };

    calculator.keys.addEventListener('click', function(event) {
        const { target } = event;
        const { value } = target;
        if (!target.matches('button')) {
            return;
        } else {
            switch (value) {
                case '=':
                    calculate(calculator);
                    break;
                case 'all-clear':
                    calculator.screenValue = '';
                    calculator.screen.value = '';
                    break;
                case 'delete':
                    calculator.screenValue = calculator.screenValue.slice(0, -1);
                    calculator.screen.value = calculator.screenValue;
                    break;
                default:
                    updateScreen(calculator, value);
                    break;
            }
        }
    });

    function calculate(calc) {
        try {
            const expression = calc.screenValue.replace('√', 'Math.sqrt').replace('^', '**');
            calc.screen.value = eval(expression);
            calc.screenValue = calc.screen.value;
        } catch (error) {
            calc.screen.value = 'Error';
        }
    }

    function updateScreen(calc, value) {
        if (calc.screenValue === '' && calc.operators.includes(value) && value !== '(') {
            return;
        }

        if (calc.operators.includes(value) && calc.operators.includes(calc.lastInput) && calc.lastInput !== ')') {
            return;
        }

        if (value === '√' && (calc.screenValue !== '' && !calc.operators.includes(calc.lastInput))) {
            return;
        }

        calc.screenValue += value;
        calc.screen.value = calc.screenValue;
        calc.lastInput = value;
    }
});
