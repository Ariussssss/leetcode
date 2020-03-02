/*
* @Author: Arius
* @Date:   2019-06-10 21:34:26
* @Last Modified by:   Arius
* @Last Modified time: 2019-06-10 23:09:57
*/



// 学生按成绩分组
function getGrade(score) {
  return score < 60 ? 'C':
    score < 80 ? 'B' : 'A';
}

function groupBy(students) {
  const res = {};
  students.forEach(student => {
    const level = getGrade(student.score);
    if (level in res) {
      res[level].push(student);
    } else {
      res[level] = [student];
    }
  });
  return res;
}

function testGroupBy() {
  const students = [{
    name: '张三',
    score: 84,
  }, {
    name: '李四',
    score: 58,
  }, {
    name: '王五',
    score: 99,
  }, {
    name: '赵六',
    score: 69,
  }]
  const res = groupBy(students);
  // console.log(JSON.stringify(res, null, 4))
  return (res['A'].length === 2 && res['B'].length === 1 &&
    res['C'].length === 1)
}



// 自增ID
function getIncName(srcName, rootTreeNode) {
  const paramNum = [];

  function getIncNameSup(treeNode){
    if (treeNode.name.includes(srcName)) {
      paramNum.push(parseInt(treeNode.name.replace(`${srcName}_`, '')));
    }
    if (treeNode.children) {
      treeNode.children.map(getIncNameSup);
    }
  }

  getIncNameSup(rootTreeNode);
  paramNum.sort((a,b) => a > b ? -1 : 1);
  let counter = 1;
  while (paramNum.length > 0) {
    const tick = paramNum.pop();
    if (tick != counter) {
      break;
    } else {
      counter += 1;
    }
  }
  return `${srcName}_${counter}`;
}

function testGetIncName() {
  const tree = {
    id: '1',
    type: 'View',
    name: 'view_1',
    children: [{
      id: '3',
      type: 'View',
      name: 'view_3',
    }]
  };
  return getIncName('view', tree) === 'view_2' 
}


 

// 字符串Parse
function parse(typeArray) {
  const startFlag = '<',
    endFlag = '>',
    step = ',';

  function parseSup(parseStr) {
    parseStr = parseStr.trim()
    if (!parseStr.includes(startFlag)) {
      return {type: parseStr};
    } else {
      const start = parseStr.indexOf(startFlag)
      let req = parseStr.slice(
              start + 1,
              parseStr.lastIndexOf(endFlag));
      let counter = 0, flag = 0;
      let params = [];
      if (!req.includes(startFlag)) {
        params = req.split(',')
      } else {
        req = Array.from(req)
        req.map((char, index) => {
          if (flag === 0 && char === step) {
            params.push(req.slice(counter, index).join(''));
            counter = index + 1;
          } else if(char === startFlag) {
            flag += 1;
          } else if(char === endFlag) {
            flag -= 1;
          }
        });
        params.push(req.slice(counter).join(''));
      }
      return {
        type: parseStr.slice(0, start),
        typeArgs: params.map(parseSup),
      };
    }
  }
  
  return parseSup(typeArray)
}

function testParse() {
  const a = parse('Array'),
    b = parse('Array<bool>'),
    c = parse('Array<Array<Array<bool>>>'),
    d = parse('Array<bool, Array<Map<string, string>, bool>, Map<string, string>, number>');
  [a,b,c,d].map(e => console.log(JSON.stringify(e, null, 4)))
}
testParse()