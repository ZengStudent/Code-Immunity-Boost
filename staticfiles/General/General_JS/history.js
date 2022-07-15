//(圓餅圖)製造白血球、疫苗
function history_doughnut_role(guard_contract_count,aggression_contract_count) {
    let data = {
        labels: [
            '製造白血球',
            '製造疫苗',
        ],
        datasets: [{
            label: '製造白血球、製造疫苗',
            data: [parseInt(guard_contract_count), parseInt(aggression_contract_count)],
            backgroundColor: [
                'rgb(94, 114, 228)',
                'rgb(245, 54, 92)'
            ],
            hoverOffset: 2
        }]
    };

    let config = {
        type: 'doughnut',
        data: data,
    };

    let historydoughnutrole_chart = new Chart(document.getElementById('history_doughnut_role'), config);
}


//(圓餅圖)Pass Condition
function history_doughnut_passcondition(mutationscore_contract_count,coverage_contract_count,unittest_contract_count) {
    let data = {
        labels: [
            'Mutation Score',
            'Coverage',
            'Unit Test',
        ],
        datasets: [{
            label: 'Pass Condition',
            data: [parseInt(mutationscore_contract_count), parseInt(coverage_contract_count), parseInt(unittest_contract_count)],
            backgroundColor: [
                'rgb(94, 114, 228)',
                'rgb(245, 54, 92)',
                'rgb(4, 150, 92)'
            ],
            hoverOffset: 2
        }]
    };

    let config = {
        type: 'doughnut',
        data: data,
    };

    let historydoughnutpasscondition_chart = new Chart(document.getElementById('history_doughnut_passcondition'), config);
}




//(圓餅圖)Pass State
function history_doughnut_passstate(basic_contract_count,advance_contract_count) {
    let data = {
        labels: [
            '完成數量(基本)',
            '完成數量(額外)',
        ],
        datasets: [{
            label: '完成數量(基本)、完成數量(額外)',
            data: [parseInt(basic_contract_count), parseInt(advance_contract_count)],
            backgroundColor: [
                'rgb(94, 114, 228)',
                'rgb(245, 54, 92)'
            ],
            hoverOffset: 2
        }]
    };

    let config = {
        type: 'doughnut',
        data: data,
    };

    let historydoughnutpassstate_chart = new Chart(document.getElementById('history_doughnut_passstate'), config);
}
