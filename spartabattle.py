import random, time

#클래스. 적.
class Enemy():
    hp = 3
    alive = True
    act = 0

    def hit(self):
        self.hp = self.hp - 1
        if self.hp == 0:
            self.alive = False
    
    def status_check(self):
        if not self.alive:
            print('적을 쓰러뜨렸다')

#클래스. 주인공.
class Sparta():
    hp = 3
    alive = True
    act = 0

    def hit(self):
        self.hp = self.hp - 1
        if self.hp == 0:
            self.alive = False
    
    def status_check(self):
        if not self.alive:
            print('내가 쓰러졌다')

#함수. 전투진행.
def battle():
    print(f'당신의 행동:{acts[m.act]}')
    print(f'상대의 행동:{acts[e.act]}')
    if m.act == e.act :
        print('비겼다')
    elif m.act - e.act == 1 or m.act - e.act == -2 :
        print('상대의 공격 성공')
        m.hit()
    elif m.act - e.act == 2 or m.act - e.act == -1 :
        print('나의 공격 성공')
        e.hit()
    

#전역변수. 턴개수, 행동선택지
m = Sparta()
e = Enemy()
turns = 0
acts = ["0","창 찌르기", "밀어 차기", "방패 올리기"]

#시작멘트
print('스파르타 배틀')

#게임진행
while(True):
    turns += 1
    print(f'[{turns}턴] 나의 체력:{m.hp} 상대 체력:{e.hp}')

    e.act = random.randint(1,3)
    print(f'당신의 행동은?1:{acts[1]},2:{acts[2]},3:{acts[3]}')
    m.act = int(input('(1/2/3):'))
    battle()
    print('')

    m.status_check()
    e.status_check()
    time.sleep(1.5)
    if m.alive == False or e.alive == False:
        break

#끝멘트
print('게임종료')