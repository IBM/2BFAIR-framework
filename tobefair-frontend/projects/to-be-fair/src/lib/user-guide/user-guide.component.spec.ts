import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UserGuideComponent } from './user-guide.component';

describe('UserGuideComponent', () => {
  let component: UserGuideComponent;
  let fixture: ComponentFixture<UserGuideComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UserGuideComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(UserGuideComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
